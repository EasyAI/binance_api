'''
Endpoints are collected from the Websocket api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams
'''

# Aggregate Trade Streams:
class set_aggTrade_stream:
    params = {'R':['symbol']}
    endpoint = '<symbol>@aggTrade'


# Trade Streams:
class set_trade_stream:
    params = {'R':['symbol']}
    endpoint = '<symbol>@trade'

# Kline/Candlestick Streams:
class set_candle_stream:
    params = {'R':['symbol', 'interval'],
            'O':['local_manager']}
    data_type = 'CANDLE'
    endpoint = '<symbol>@kline_<interval>'


# Individual Symbol Mini Ticker Stream:
class set_miniTicker_stream:
    params = {'R':['symbol']}
    endpoint = '<symbol>@miniTicker'


# All Market Mini Tickers Stream:
class set_global_miniTicker_stream:
    params = None
    endpoint = '!miniTicker@arr'


# Individual Symbol Ticker Streams:
class set_ticker_stream:
    params = {'R':['symbol']}
    endpoint = '<symbol>@ticker'


# All Market Tickers Stream:
class set_gloal_ticker_stream:
    params = None
    endpoint = '!ticker@arr'


# Individual Symbol Book Ticker Streams:
class set_bookTicker_stream:
    params = {'R':['symbol']}
    endpoint = '<symbol>@bookTicker'


# All Book Tickers Stream:
class set_global_bookTicker_stream:
    params = None
    endpoint = '!bookTicker'


# Partial Book Depth Streams:
class set_partialBookDepth_stream:
    params = {'R':['symbol', 'levels'],
            'O':['update_speed']}
    endpoint = '<symbol>@depth<levels>@<update_speed>'


# Diff. Depth Stream:
class set_manual_depth_stream:
    params = {'R':['symbol'],
            'O':['update_speed']}
    data_type = 'BOOKS'
    endpoint = '<symbol>@depth@<update_speed>'