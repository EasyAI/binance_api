class set_aggTrade_stream:
    params = {'R':['symbol']}
    endpoint = '<symbol>@aggTrade'


class set_trade_stream:
    params = {'R':['symbol']}
    endpoint = '<symbol>@trade'


class set_candle_stream:
    params = {'R':['symbol', 'interval'],
            'O':['local_manager']}
    data_type = 'CANDLE'
    endpoint = '<symbol>@kline_<interval>'


class set_miniTicker_stream:
    params = {'R':['symbol']}
    endpoint = '<symbol>@miniTicker'


class set_global_miniTicker_stream:
    params = None
    endpoint = '!miniTicker@arr'


class set_ticker_stream:
    params = {'R':['symbol']}
    endpoint = '<symbol>@ticker'


class set_gloal_ticker_stream:
    params = None
    endpoint = '!ticker@arr'


class set_bookTicker_stream:
    params = {'R':['symbol']}
    endpoint = '<symbol>@bookTicker'


class set_global_bookTicker_stream:
    params = None
    endpoint = '!bookTicker'


class set_partialBookDepth_stream:
    params = {'R':['symbol', 'levels'],
            'O':['update_speed']}
    endpoint = '<symbol>@depth<levels>@<update_speed>'


class set_manual_depth_stream:
    params = {'R':['symbol'],
            'O':['update_speed']}
    data_type = 'BOOKS'
    endpoint = '<symbol>@depth@<update_speed>'