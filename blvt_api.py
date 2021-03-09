'''
Endpoints are collected from the BLVT Endpoints api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#blvt-endpoints
'''

# Get BLVT Info:
class get_blvt_info:
    params = {'O':['tokenName']}
    method = 'GET'
    endpoint = '/sapi/v1/blvt/tokenInfo'
    security_type = 'MARKET_DATA'


# Historical BLVT NAV Kline/Candlestick:
class get_blvt_historic_candles:
    '''
    Endpoint is based on binance future endpoint (fapi)
    '''
    pass


# Subscribe BLVT:
class subscribe_blvt:
    params = {'R':['tokenName', 'cost']}
    method = 'POST'
    endpoint = '/sapi/v1/blvt/subscribe'
    security_type = 'USER_DATA'


# Query Subscription Record:
class query_subscription_record:
    params = {'O':['tokenName', 'id', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/blvt/subscribe/record'
    security_type = 'USER_DATA'


# Redeem BLVT:
class redeem_blvt:
    params = {'R':['tokenName', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/blvt/redeem'
    security_type = 'USER_DATA'


# Query Redemption Record:
class query_redemption_record:
    params = {'O':['tokenName', 'id', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/blvt/redeem/record'
    security_type = 'USER_DATA'


# Get BLVT User Limit Info:
class get_blvt_userLimit:
    params = {'O':['tokenName']}
    method = 'GET'
    endpoint = '/sapi/v1/blvt/userLimit'
    security_type = 'USER_DATA'


# Websocket BLVT Info Streams:
class blvt_info_stream:
    '''
    Endpoint is based on binance future websocket (fstream or fstream3)
    '''
    pass


# BLVT NAV Kline/Candlestick Streams:
class blvt_candle_stream:
    '''
    Endpoint is based on binance future websocket (fstream or fstream3)
    '''
    pass