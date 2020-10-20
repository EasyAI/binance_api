#! /usr/bin/env python3

import time
import json
import logging

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
            trades = rest_master.Binance_REST().get_recent_trades(
                symbol=kwargs['symbol'],
                limit=t_limit)
        else:
            time.sleep(0.75)
            trades = authApi.get_historical_trades(
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
    elif interval_time_type == 'w':
        best_interval = best_interval_calc(BASE_BINANCE_WEEKS, interval_number_multiplier, 0)
    else:
        return('INVALIDE_TIMEFRAME')

    if best_interval == None:
        return('ERROR_INVALID_INTEVAL')

    if best_interval == interval_number_multiplier:
        total_candles_left = int(kwargs['limit'])
    else:
        total_candles_left = int(kwargs['limit']*(interval_number_multiplier/best_interval))

    best_interval = '{0}{1}'.format(best_interval, interval_time_type)

    while True:
        if total_candles_left > 1000:
            total_candles_left -= 1000
            c_limit = 1000

        else:
            if total_candles_left == 0:
                break
            else:
                c_limit = total_candles_left
                total_candles_left = 0

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

    if best_interval != kwargs['interval']:
        for candle in candle_data:
            pass

    return(candle_data)


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