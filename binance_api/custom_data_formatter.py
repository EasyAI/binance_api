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

def get_custom_candles(kwargs):

    candle_data = []

    ##
    interval_time_type = kwargs['interval'][-1]

    ##
    interval_number_multiplier = kwargs['interval'][:-1]

    total_candles_left = kwargs['limit']

    c_limit = 0
    c_start_time = 0 if not 'startTime' in kwargs else kwargs['startTime']
    c_end_time = 0

    if interval_time_type == 'm' and not(interval_number_multiplier in kwargs['interval']):
        pass
    else: 
        best_interval = kwargs['interval']

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

    return(candle_data)
