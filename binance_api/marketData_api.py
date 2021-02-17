'''
Endpoints are collected from the Market Data Endpoints api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#market-data-endpoints
'''

# Test Connectivity:
class test_ping:
    params = None
    method = 'GET'
    endpoint = '/api/v3/ping'
    security_type = 'None'


# Check Server Time:
class get_serverTime:
    params = None
    method = 'GET'
    endpoint = '/api/v3/time'
    security_type = 'None'


# Exchange Information:
class get_exchangeInfo:
    params = None
    method = 'GET'
    endpoint = '/api/v3/exchangeInfo'
    security_type = 'None'


# Order Book:
class get_orderBook:
    params = {'R':['symbol'],
            'O':['limit']}
    method = 'GET'
    endpoint = '/api/v3/depth'
    security_type = 'None'


# Recent Trades List:
class get_recentTrades:
    params = {'R':['symbol'],
            'O':['limit']}
    method = 'GET'
    endpoint = '/api/v3/trades'
    security_type = 'None'


# Old Trade Lookup:
class get_oldTrades:
    params = {'R':['symbol'],
            'O':['limit', 'fromId']}
    method = 'GET'
    endpoint = '/api/v3/historicalTrades'
    security_type = 'None'


# Compressed/Aggregate Trades List:
class get_aggTradeList:
    params = {'R':['symbol'],
            'O':['limit', 'fromId', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/api/v3/aggTrades'
    security_type = 'None'


# Kline/Candlestick Data:
class get_candles:
    params = {'R':['symbol', 'interval'],
            'O':['startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/api/v3/klines'
    security_type = 'None'


# Current Average Price:
class get_averagePrice:
    params = {'R':['symbol']}
    method = 'GET'
    endpoint = '/api/v3/avgPrice'
    security_type = 'None'


# 24hr Ticker Price Change Statistics:
class get_24hTicker:
    params = {'O':['symbol']}
    method = 'GET'
    endpoint = '/api/v3/ticker/24hr'
    security_type = 'None'


# Symbol Price Ticker:
class get_priceTicker:
    params = {'O':['symbol']}
    method = 'GET'
    endpoint = '/api/v3/ticker/price'
    security_type = 'None'


# Symbol Order Book Ticker:
class get_orderbookTicker:
    params = {'O':['symbol']}
    method = 'GET'
    endpoint = '/api/v3/ticker/bookTicker'
    security_type = 'None'