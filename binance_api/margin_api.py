'''
Endpoints are collected from the Margin Endpoints api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#margin-account-trade
'''

# Cross Margin Account Transfer:
class place_order:
    params = {'R':['asset', 'amount', 'type']}
    method = 'POST'
    endpoint = '/sapi/v1/margin/transfer'
    security_type = 'MARGIN'


# Margin Account Borrow:
class place_order:
    params = {'R':['asset', 'amount'],
            'O':['isIsolated', 'symbol']}
    method = 'POST'
    endpoint = '/sapi/v1/margin/loan'
    security_type = 'MARGIN'


# Margin Account Repay:
class place_order:
    params = {'R':['asset', 'amount'],
            'O':['isIsolated', 'symbol']}
    method = 'POST'
    endpoint = '/sapi/v1/margin/repay'
    security_type = 'MARGIN'


# Query Margin Asset:
class place_order:
    params = {'R':['asset']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/asset'
    security_type = 'MARKET_DATA'


# Query Cross Margin Pair:
class place_order:
    params = {'R':['symbol']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/pair'
    security_type = 'MARKET_DATA'

# Get All Margin Assets:
class place_order:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/margin/allAssets'
    security_type = 'MARKET_DATA'


# Get All Cross Margin Pairs:
class place_order:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/margin/allPairs'
    security_type = 'MARKET_DATA'


# Query Margin PriceIndex:
class place_order:
    params = {'R':['symbol']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/priceIndex'
    security_type = 'MARKET_DATA'


# Margin Account New Order:
class place_order:
    params = {'R':['symbol', 'side', 'type'],
            'O':['isIsolated', 'quantity', 'quoteOrderQty', 'price', 'stopPrice', 'newClientOrderId', 'icebergQty', 'newOrderRespType', 'sideEffectType', 'timeInForce']}
    method = 'POST'
    endpoint = '/sapi/v1/margin/order'
    security_type = 'TRADE'


# Margin Account Cancel Order:
class place_order:
    params = {'R':['symbol'],
            'O':['isIsolated', 'orderId', 'origClientOrderId', 'newClientOrderId']}
    method = 'DELETE'
    endpoint = '/sapi/v1/margin/order'
    security_type = 'TRADE'


# Margin Account Cancel all Open Orders on a Symbol:
class place_order:
    params = {'R':['symbol'],
            'O':['isIsolated']}
    method = 'DELETE'
    endpoint = '/sapi/v1/margin/openOrders'
    security_type = 'TRADE'


# Get Cross Margin Transfer History:
class place_order:
    params = {'O':['asset', 'type', 'startTime', 'endTime', 'current', 'size', 'archived']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/transfer'
    security_type = 'USER_DATA'


# Query Loan Record:
class place_order:
    params = {'R':['asset'],
            'O':['isolatedSymbol', 'txId', 'startTime', 'endTime', 'current', 'size', 'archived']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/loan'
    security_type = 'USER_DATA'


# Query Repay Record:
class place_order:
    params = {'R':['asset'],
            'O':['isolatedSymbol', 'txId', 'startTime', 'endTime', 'current', 'size', 'archived']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/repay'
    security_type = 'USER_DATA'


# Get Interest History:
class place_order:
    params = {'O':['asset', 'isolatedSymbol', 'startTime', 'endTime', 'current', 'size', 'archived']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/interestHistory'
    security_type = 'USER_DATA'


# Get Force Liquidation Record:
class place_order:
    params = {'O':['startTime', 'endTime', 'isolatedSymbol', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/forceLiquidationRec'
    security_type = 'USER_DATA'


# Query Cross Margin Account Details:
class place_order:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/margin/account'
    security_type = 'USER_DATA'


# Query Margin Account's Order:
class place_order:
    params = {'R':['symbol'],
            'O':['isIsolated', 'orderId', 'origClientOrderId']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/order'
    security_type = 'USER_DATA'


# Query Margin Account's Open Orders:
class place_order:
    params = {'O':['symbol', 'isIsolated']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/openOrders'
    security_type = 'USER_DATA'


# Query Margin Account's All Orders:
class place_order:
    params = {'R':['symbol'],
            'O':['isIsolated', 'orderId', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/allOrders'
    security_type = 'USER_DATA'


# Query Margin Account's Trade List:
class place_order:
    params = {'R':['symbol'],
            'O':['isIsolated', 'startTime', 'endTime', 'fromId', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/myTrades'
    security_type = 'USER_DATA'


# Query Max Borrow:
class place_order:
    params = {'R':['asset'],
            'O':['isolatedSymbol']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/maxBorrowable'
    security_type = 'USER_DATA'


# Query Max Transfer-Out Amount:
class place_order:
    params = {'R':['asset'],
            'O':['isolatedSymbol']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/maxTransferable'
    security_type = 'USER_DATA'


# Create Isolated Margin Account:
class place_order:
    params = {'R':['base', 'quote']}
    method = 'POST'
    endpoint = '/sapi/v1/margin/isolated/create'
    security_type = 'MARGIN'


# Isolated Margin Account Transfer:
class place_order:
    params = {'R':['asset', 'symbol', 'transFrom', 'transTo', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/margin/isolated/transfer'
    security_type = 'MARGIN'


# Get Isolated Margin Transfer History:
class place_order:
    params = {'R':['symbol'],
            'O':['asset', 'symbol', 'transFrom', 'transTo', 'startTime', 'endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/isolated/transfer'
    security_type = 'USER_DATA'


# Query Isolated Margin Account Info
class place_order:
    params = {'O':['symbols']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/isolated/account'
    security_type = 'USER_DATA'


# Query Isolated Margin Symbol:
class place_order:
    params = {'R':['symbol'],
    'O':['price']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/isolated/pair'
    security_type = 'USER_DATA'


# Get All Isolated Margin Symbol:
class place_order:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/margin/isolated/allPairs'
    security_type = 'USER_DATA'


# Toggle BNB Burn On Spot Trade And Margin Interest:
class place_order:
    params = {'O':['spotBNBBurn', 'interestBNBBurn']}
    method = 'POST'
    endpoint = '/sapi/v1/bnbBurn'
    security_type = 'USER_DATA'


# Get BNB Burn Status:
class place_order:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/bnbBurn'
    security_type = 'USER_DATA'

