#! /usr/bin/env python3

import re
import time
import json
import logging
from datetime import datetime

from . import api_master_rest_caller

BASE_1m = (60*1000)
BASE_1h = BASE_1m*60
BASE_1d = BASE_1h*24
BASE_1w = BASE_1d*7

BASE_BINANCE_MINS   = [1, 3, 5, 15, 30]
BASE_BINANCE_HOURS  = [1, 2, 4, 6, 8, 12]
BASE_BINANAE_DAYS   = [1, 3]
BASE_BINANCE_WEEKS  = [1]


def _combined_param_list(api_info):
    all_params_cat = {'R':{},'O':{}}
    all_params_uncat = []
    # Check for url parameters/url fillin parameters

    for param_type in ['R','O']: # Check for Required and Optional parameters.
        for data_type in ['P', 'H', 'B']: # Check for Parameters (url params/fillin gaps), Headers, Post Body.
            try:
                if data_type == 'P':
                    target_data_type = api_info.params
                elif data_type == 'H':
                    target_data_type = api_info.headers
                elif data_type == 'B':
                    target_data_type = api_info.body
            except AttributeError as error:
                # If no data is available just set as null and pass.
                target_data_type = None

            # Check if there is data availible.
            if target_data_type != None:
                if param_type in target_data_type:
                    all_params_cat[param_type].update({data_type:[]})
                    all_params_cat[param_type][data_type].extend(target_data_type[param_type])

    # Get a list of all the parameters by themselves.
    for req_op in all_params_cat:
        for data_types in all_params_cat[req_op]:
            for key_value in all_params_cat[req_op][data_types]:
                if not(key_value in all_params_uncat):
                    all_params_uncat.append(key_value)

    return(all_params_cat, all_params_uncat)


def param_check(api_info, users_passed_parameters={}):
    params = {}
    headers = {}
    body = {}

    # Check for any URL parameters that need populated.
    target_endpoint = api_info.endpoint
    missing_url_params = []
    if '<' in target_endpoint and '>' in target_endpoint:
        url_variables = re.findall(r'<([^>]+)>', target_endpoint)
        for val in url_variables:
            if val in users_passed_parameters:
                target_endpoint = target_endpoint.replace("<{0}>".format(val), users_passed_parameters[val])
                del users_passed_parameters[val]
            else:
                missing_url_params.append(val)

    if len(missing_url_params) >= 1:
        return('MISSING_REQUIRED_PARAMETERS', missing_url_params)

    organised_params, full_params_list = _combined_param_list(api_info)

    ## Update parameter checks
    if full_params_list != []:
        # Check if ALL required parameters are passed and if not return a message saying what are missing.
        missingParameters = []
        for data_type in organised_params['R']:
            for key_value in organised_params['R'][data_type]:
                if not key_value in users_passed_parameters:
                    missingParameters.append(key_value)

        if len(missingParameters) >= 1:
            return('MISSING_REQUIRED_PARAMETERS', missingParameters)

        # Sort the passed data to the correct variable types (body, header, urlparams)
        for req_op in organised_params:
            for data_types in organised_params[req_op]:
                current_kv_required = organised_params[req_op][data_types]
                for key_value in users_passed_parameters:
                    if key_value in current_kv_required:
                        if data_types == 'P':
                            params.update({key_value:users_passed_parameters[key_value]})
                        elif data_types == 'H':
                            headers.update({key_value:users_passed_parameters[key_value]})
                        elif data_types == 'B':
                            body.update({key_value:users_passed_parameters[key_value]})

    else:
        if users_passed_parameters != None and users_passed_parameters != {}:
            return('ENDPOINT_TAKES_NO_PARAMETERS_BUT_SOME_WHERE_GIVEN', users_passed_parameters)

    return(target_endpoint, params, headers, body)



def get_custom_trades(kwargs):
    ''' '''
    trade_data = []
    total_trades_left = kwargs['limit']
    t_id = 0

    if total_trades_left > 1000:
        authApi = api_master_rest_caller.Binance_REST(kwargs['pubKey'], kwargs['prvKey'])

    while True:
        if total_trades_left > 1000:
            total_trades_left -= 1000
            t_limit = 1000

        else:
            if total_trades_left == 0:
                break
            else:
                t_limit = total_trades_left
                total_trades_left = 0

        if t_id == 0:
            trades = api_master_rest_caller.Binance_REST().get_recentTrades(
                symbol=kwargs['symbol'],
                limit=t_limit)
        else:
            time.sleep(0.75)
            trades = authApi.get_oldTrades(
                symbol=kwargs['symbol'], 
                limit=t_limit, 
                fromId=t_id)

        t_id = trades[-1]['id']
        trade_data = trade_data + trades

    return(trade_data)


def get_custom_candles(kwargs):
    ''' '''
    candle_data = []

    ##
    interval_time_type = kwargs['interval'][-1]

    ##
    interval_number_multiplier = int(kwargs['interval'][:-1])

    total_candles_left = kwargs['limit']

    c_limit = 0
    c_start_time = 0 if not 'startTime' in kwargs else kwargs['startTime']
    c_end_time = 0
    best_interval = None

    if interval_time_type == 'm':
        best_interval = best_interval_calc(BASE_BINANCE_MINS, interval_number_multiplier, 60)
    elif interval_time_type == 'h':
        best_interval = best_interval_calc(BASE_BINANCE_HOURS, interval_number_multiplier, 24)
    elif interval_time_type == 'd':
        best_interval = best_interval_calc(BASE_BINANAE_DAYS, interval_number_multiplier, 7)
    else:
        return('INVALIDE_TIMEFRAME')

    if best_interval == None:
        return('ERROR_INVALID_INTEVAL')

    if best_interval == interval_number_multiplier:
        total_candles_left = int(kwargs['limit'])
    else:
        total_candles_left = int(kwargs['limit']*(interval_number_multiplier/best_interval))

    best_interval = '{0}{1}'.format(best_interval, interval_time_type)

    total_sets_done = 0
    total_sets = total_candles_left/1000

    print('Total 1k sets: {0}'.format(total_sets))

    while True:

        total_left_Time = (total_sets-total_sets_done)*1.2

        if total_left_Time > 60:
            time_min, time_sec = str(total_left_Time/60).split('.')

            time_sec = (int(time_sec[:2])/100)*60

            f_total_time = '{0}.{1:.0f}m'.format(int(time_min), time_sec)
        else:
            f_total_time = '{0}s'.format(int(total_left_Time))


        print('Candle sets: {0}/{1}, ETA: {2}'.format(total_sets_done, total_sets, f_total_time))

        if total_candles_left > 1000:
            total_candles_left -= 1000
            c_limit = 1000

        else:
            if total_candles_left == 0:
                break
            else:
                c_limit = total_candles_left
                total_candles_left = 0

        total_sets_done += c_limit/1000

        if c_end_time == 0:
            candles = api_master_rest_caller.Binance_REST().get_candles(
                symbol=kwargs['symbol'], 
                interval=best_interval, 
                limit=c_limit)
        else:
            time.sleep(0.75)
            candles = api_master_rest_caller.Binance_REST().get_candles(
                symbol=kwargs['symbol'], 
                interval=best_interval, 
                limit=c_limit, 
                endTime=c_end_time)

        c_end_time = candles[-1][0]-1
        candle_data = candle_data + candles

    ## To be used to build custom timeframes
    if best_interval != kwargs['interval']:

        # Build the most recent candles close time into a valid timestamp.
        cc_time=round((candle_data[0][6]/1000))

        if interval_time_type == 'm':
            current_time = time.localtime()[4]
            split_time = int(str(datetime.fromtimestamp(cc_time))[11:].split(':')[1])
        elif interval_time_type == 'h':
            current_time = time.localtime()[3]
            split_time = int(str(datetime.fromtimestamp(cc_time))[11:].split(':')[0])
        elif interval_time_type == 'd':
            current_time = time.localtime()[2]
            split_time = int(str(datetime.fromtimestamp(cc_time))[:10].split('-')[2])

        # How many candles required for the current candle with the new timeframe.
        current_range = round((split_time%interval_number_multiplier)/int(best_interval[:-1]))

        # This holds the amount of candles will be part of 1 with the new timeframe.
        normal_range = round(interval_number_multiplier/int(best_interval[:-1]))

        # max amount of candles for new timeframe.
        candles_for_new_timeframe = round(len(candle_data)/normal_range)-1

        # New empty list where the newly built candles will be held
        buit_candles = []

        for i in range(candles_for_new_timeframe):
            ccstart = i*current_range
            ccend   = (i*current_range)+current_range

            otime       = candle_data[ccend-1][0]
            copen       = candle_data[ccend-1][1]
            chigh       = 0
            clow        = 9999
            cclose      = candle_data[ccstart][4]
            cvolume     = 0
            closetime   = candle_data[ccstart][6]
            qavolume    = 0
            numtrades   = 0

            for x, candle in enumerate(candle_data[ccstart:ccend]):
                chigh = candle[2] if candle[2] > chigh else chigh
                clow = candle[3] if candle[3] < clow else clow
                cvolume += candle[5]
                qavolume += candle[7]
                numtrades += candle[8]
            
            buit_candles.append([otime, copen, chigh, clow, cclose, cvolume, closetime, qavolume, numtrades])

            current_range = normal_range

        return_candles = buit_candles
    else:
        return_candles = candle_data

    return(return_candles)


def best_interval_calc(base_intervals, target_interval, max_time):
    best_interval = None

    if max_time == 0:
        return(target_interval)

    if not(target_interval in base_intervals) and (max_time % target_interval == 0):
        for current_interval in base_intervals:
            if (current_interval < target_interval) and (target_interval % current_interval == 0):
                best_interval = current_interval
            elif current_interval > target_interval:
                break

    if target_interval in base_intervals:
        best_interval = target_interval

    return(best_interval)