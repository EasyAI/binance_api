
class transfer_to_margin:
    params = {'R':['asset', 'amount', 'type']}
    method = 'POST'
    endpoint = '/sapi/v1/margin/transfer'
    security_type = 'MARGIN'


class apply_for_loan:
    params = {'R':['asset', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/margin/loan'
    security_type = 'MARGIN'


class repay_loan:
    params = {'R':['asset', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/margin/repay'
    security_type = 'MARGIN'


class place_order:
    params = {'R':['symbol', 'side', 'type', 'quantity'],
    'O':['price', 'stopPrice', 'newClientOrderId', 'icebergQty', 'newOrderRespType', 'timeInForce']}
    method = 'POST'
    endpoint = '/sapi/v1/margin/order'
    security_type = 'TRADE'


class cancel_order:
    params = {'R':['symbol'],
    'O':['orderId', 'origClientOrderId', 'newClientOrderId']}
    method = 'DELETE'
    endpoint = '/sapi/v1/margin/order'
    security_type = 'TRADE'


class get_loan_record:
    params = {'R':['asset'],
    'O':['txId', 'startTime', 'endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/loan'
    security_type = 'USER_DATA'


class get_repayed_record:
    params = {'R':['asset'],
    'O':['txId', 'startTime', 'endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/repay'
    security_type = 'USER_DATA'


class get_account:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/margin/account'
    security_type = 'USER_DATA'


class get_asset:
    params = {'R':['asset']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/asset'
    security_type = 'MARKET_DATA'


class get_market_info:
    params = {'R':['symbol']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/pair'
    security_type = 'MARKET_DATA'


class get_all_assets:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/margin/allAssets'
    security_type = 'MARKET_DATA'


class get_all_markets:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/margin/allPairs'
    security_type = 'MARKET_DATA'


class get_margin_priceIndex:
    params = {'R':['symbol']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/priceIndex'
    security_type = 'MARKET_DATA'


class get_transfer_history:
    params = {'R':['type'],
    		'O':['asset', 'startTime', 'endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/transfer'
    security_type = 'USER_DATA'


class get_interest_history:
    params = {'O':['asset', 'startTime', 'endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/interestHistory'
    security_type = 'USER_DATA'


class get_liquidation_record:
    params = {'O':['startTime', 'endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/forceLiquidationRec'
    security_type = 'USER_DATA'


class get_market_orders:
    params = {'R':['symbol'],
    		'O':['orderId', 'origClientOrderId']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/order'
    security_type = 'USER_DATA'


class get_open_orders:
    params = {'O':['symbol']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/openOrders'
    security_type = 'USER_DATA'


class get_all_orders:
    params = {'R':['symbol'],
    		'O':['orderId', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/allOrders'
    security_type = 'USER_DATA'


class get_all_trades:
    params = {'R':['symbol'],
    		'O':['startTime', 'endTime', 'fromId', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/myTrades'
    security_type = 'USER_DATA'


class get_max_borrow_amount:
    params = {'R':['asset']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/maxBorrowable'
    security_type = 'USER_DATA'


class get_max_transfer_amount:
    params = {'R':['asset']}
    method = 'GET'
    endpoint = '/sapi/v1/margin/maxTransferable'
    security_type = 'USER_DATA'