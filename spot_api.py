'''
Endpoints are collected from the Spot Endpoints api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#spot-account-trade
'''

# Test New Order:
class place_order_test:
    params = {'R':['symbol', 'side', 'type'], 
            'O':['timeInForce', 'quantity', 'quoteOrderQty', 'price', 'newClientOrderId', 'stopPrice', 'icebergQty', 'newOrderRespType']}
    method = 'POST'
    endpoint = '/api/v3/order/test'
    security_type = 'TRADE'


# New Order:
class place_order:
    params = {'R':['symbol', 'side', 'type'], 
            'O':['timeInForce', 'quantity', 'quoteOrderQty', 'price', 'newClientOrderId', 'stopPrice', 'icebergQty', 'newOrderRespType']}
    method = 'POST'
    endpoint = '/api/v3/order'
    security_type = 'TRADE'


# Cancel Order:
class cancel_order:
    params = {'R':['symbol'], 
            'O':['orderId', 'origClientOrderId', 'newClientOrderId']}
    method = 'DELETE'
    endpoint = '/api/v3/order'
    security_type = 'TRADE'


# Cancel all Open Orders on a Symbol:
class cancel_all_orders:
    params = {'R':['symbol']}
    method = 'DELETE'
    endpoint = '/api/v3/openOrders'
    security_type = 'TRADE'


# Query Order:
class get_order:
    params = {'R':['symbol'], 
            'O':['orderId', 'origClientOrderId']}
    method = 'GET'
    endpoint = '/api/v3/order'
    security_type = 'USER_DATA'


# Current Open Orders:
class get_open_orders:
    params = {'R':['symbol']}
    method = 'GET'
    endpoint = '/api/v3/openOrders'
    security_type = 'USER_DATA'


# All Orders:
class get_all_orders:
    params = {'R':['symbol'], 
            'O':['orderId', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/api/v3/allOrders'
    security_type = 'USER_DATA'


# New OCO:
class place_order_oco:
    params = {'R':['symbol', 'side', 'quantity', 'price', 'stopPrice'], 
            'O':['listClientOrderId', 'limitClientOrderId', 'limitIcebergQty', 'stopClientOrderId', 'stopLimitPrice', 'stopIcebergQty', 'stopLimitTimeInForce', 'newOrderRespType']}
    method = 'POST'
    endpoint = '/api/v3/order/oco'
    security_type = 'TRADE'


# Cancel OCO:
class cancel_order_oco:
    params = {'R':['symbol'], 
            'O':['orderListId', 'listClientOrderId', 'newClientOrderId']}
    method = 'DELETE'
    endpoint = '/api/v3/orderList'
    security_type = 'TRADE'


# Query OCO:
class query_order_oco:
    params = {'O':['orderListId', 'origClientOrderId']}
    method = 'GET'
    endpoint = '/api/v3/orderList'
    security_type = 'USER_DATA'


# Query all OCO:
class get_all_orders_oco:
    params = {'O':['fromId', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/api/v3/allOrderList'
    security_type = 'USER_DATA'


# Query Open OCO:
class get_open_orders_oco:
    params = None
    method = 'GET'
    endpoint = '/api/v3/openOrderList'
    security_type = 'USER_DATA'


# Account Information:
class get_accountInfo:
    params = None
    method = 'GET'
    endpoint = '/api/v3/account'
    security_type = 'USER_DATA'


# Account Trade List:
class get_all_trades:
    params = {'R':['symbol'], 
            'O':['startTime', 'endTime', 'fromId', 'limit']}
    method = 'GET'
    endpoint = '/api/v3/myTrades'
    security_type = 'USER_DATA'