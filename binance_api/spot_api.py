# Data for ping_test:
class test_ping:
    params = None
    method = 'GET'
    endpoint = '/api/v3/ping'
    security_type = 'NONE'


# Data for check_time:
class check_time:
    params = None
    method = 'GET'
    endpoint = '/api/v3/time'
    security_type = 'NONE'


# Data for get_exchange_info:
class get_exchange_info:
    params = None
    method = 'GET'
    endpoint = '/api/v3/exchangeInfo'
    security_type = 'NONE'


# Data for get_market_depth:
class get_market_depth:
    params = {'R':['symbol'], 
            'O':['limit']}
    method = 'GET'
    endpoint = '/api/v3/depth'
    security_type = 'NONE'


# Data for get_recent_trades:
class get_recent_trades:
    params = {'R':['symbol'], 
            'O':['limit']}
    method = 'GET'
    endpoint = '/api/v3/trades'
    security_type = 'NONE'


# Data for get_historical_trades:
class get_historical_trades:
    params = {'R':['symbol'], 
            'O':['limit', 'fromId']}
    method = 'GET'
    endpoint = '/api/v3/historicalTrades'
    security_type = 'MARKET_DATA'


# Data for get_agg_trades:
class get_agg_trades:
    params = {'R':['symbol'], 
            'O':['limit', 'startTime', 'endTime', 'fromId']}
    method = 'GET'
    endpoint = '/api/v3/aggTrades'
    security_type = 'NONE'


# Data for get_candles:
class get_candles:
    params = {'R':['symbol', 'interval'], 
            'O':['limit', 'startTime', 'endTime']}
    method = 'GET'
    endpoint = '/api/v3/klines'
    security_type = 'NONE'


# Data for get_avg_price:
class get_avg_price:
    params = {'R':['symbol']}
    method = 'GET'
    endpoint = '/api/v3/avgPrice'
    security_type = 'NONE'


# Data for get_market_24h:
class get_market_24h:
    params = {'O':['symbol']}
    method = 'GET'
    endpoint = '/api/v3/ticker/24hr'
    security_type = 'NONE'


# Data for get_latest_price:
class get_latest_price:
    params = {'O':['symbol']}
    method = 'GET'
    endpoint = '/api/v3/ticker/price'
    security_type = 'NONE'


# Data for get_book_ticker:
class get_book_ticker:
    params = {'O':['symbol']}
    method = 'GET'
    endpoint = '/api/v3/ticker/bookTicker'
    security_type = 'NONE'


class place_order:
    params = {'R':['symbol', 'side', 'type'], 
            'O':['timeInForce', 'quantity', 'quoteOrderQty', 'price', 'newClientOrderId', 'stopPrice', 'icebergQty', 'newOrderRespType']}
    method = 'POST'
    endpoint = '/api/v3/order'
    security_type = 'TRADE'
    

class get_order:
    params = {'R':['symbol'], 
            'O':['orderId', 'origClientOrderId']}
    method = 'GET'
    endpoint = '/api/v3/order'
    security_type = 'USER_DATA'


class cancel_order:
    params = {'R':['symbol'], 
            'O':['orderId', 'origClientOrderId', 'newClientOrderId']}
    method = 'DELETE'
    endpoint = '/api/v3/order'
    security_type = 'TRADE'


class cancel_open_orders:
    params = {'R':['symbol']}
    method = 'DELETE'
    endpoint = '/api/v3/openOrders'
    security_type = 'TRADE'


class get_open_orders:
    params = {'O':['symbol']}
    method = 'GET'
    endpoint = '/api/v3/openOrders'
    security_type = 'USER_DATA'


class get_all_orders:
    params = {'R':['symbol'],
            'O':['orderId', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/api/v3/allOrders'
    security_type = 'USER_DATA'


class place_oco_order:
    params = {'R':['symbol', 'side', 'quantity', 'price', 'stopPrice'],
            'O':['listClientOrderId', 'limitClientOrderId', 'limitIcebergQty', 'stopClientOrderId', 'stopLimitPrice', 'stopIcebergQty', 'stopLimitTimeInForce', 'newOrderRespType']}
    method = 'POST'
    endpoint = '/api/v3/order/oco'
    security_type = 'TRADE'


class cancel_oco_order:
    params = {'R':['symbol'],
            'O':['orderListId', 'listClientOrderId', 'newClientOrderId']}
    method = 'DELETE'
    endpoint = '/api/v3/orderList'
    security_type = 'TRADE'


class get_oco_order:
    params = {'O':['orderListId', 'origClientOrderId']}
    method = 'GET'
    endpoint = '/api/v3/orderList'
    security_type = 'USER_DATA'


class get_all_oco_orders:
    params = {'O':['fromId', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/api/v3/allOrderList'
    security_type = 'USER_DATA'


class get_open_oco_orders:
    params = None
    method = 'GET'
    endpoint = '/api/v3/openOrderList'
    security_type = 'USER_DATA'


class get_account:
    params = None
    method = 'GET'
    endpoint = '/api/v3/account'
    security_type = 'USER_DATA'


class get_all_trades:
    params = {'R':['symbol'],
            'O':['startTime', 'endTime', 'fromId', 'limit']}
    method = 'GET'
    endpoint = '/api/v3/orderList'
    security_type = 'USER_DATA'