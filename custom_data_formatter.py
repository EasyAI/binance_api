#! /usr/bin/env python3

import time
import json
import logging
from datetime import datetime

from . import rest_master

BASE_1m = (60*1000)
BASE_1h = BASE_1m*60
BASE_1d = BASE_1h*24
BASE_1w = BASE_1d*7

BASE_BINANCE_MINS   = [1, 3, 5, 15, 30]
BASE_BINANCE_HOURS  = [1, 2, 4, 6, 8, 12]
BASE_BINANAE_DAYS   = [1, 3]
BASE_BINANCE_WEEKS  = [1]


def get_custom_trades(kwargs):
    ''' '''
    trade_data = []
    total_trades_left = kwargs['limit']
    t_id = 0

    if total_trades_left > 1000:
        authApi = rest_master.Binance_REST(kwargs['pubKey'], kwargs['prvKey'])

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
            trades = rest_master.Binance_REST().get_recentTrades(
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
            candles = rest_master.Binance_REST().get_candles(
                symbol=kwargs['symbol'], 
                interval=best_interval, 
                limit=c_limit)
        else:
            time.sleep(0.75)
            candles = rest_master.Binance_REST().get_candles(
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