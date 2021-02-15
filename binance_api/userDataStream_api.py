'''
Endpoints are collected from the User Data Stream Endpoints api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#user-data-streams

Account Update Event: outboundAccountPosition
Order Update Event: executionReport (Also ListStatus if OCO)

'''

### SPOT ENDPOINTS ###

# Create a ListenKey:
class get_listenKey_spot:
    params = None
    method = 'POST'
    endpoint = '/api/v3/userDataStream'
    security_type = 'USER_STREAM'


# Ping/Keep-alive a ListenKey:
class send_listenKey_keepAlive_spot:
    params = {'R':['listenKey']}
    method = 'PUT'
    endpoint = '/api/v3/userDataStream'
    security_type = 'USER_STREAM'


# Close a ListenKey:
class close_listenKey_spot:
    params = {'R':['listenKey']}
    method = 'DELETE'
    endpoint = '/api/v3/userDataStream'
    security_type = 'USER_STREAM'


### MARGIN ENDPOINTS ###

# Create a ListenKey:
class get_listenKey_margin:
    params = None
    method = 'POST'
    endpoint = '/sapi/v1/userDataStream'
    security_type = 'USER_STREAM'


# Ping/Keep-alive a ListenKey:
class send_listenKey_keepAlive_margin:
    params = {'R':['listenKey']}
    method = 'PUT'
    endpoint = '/sapi/v1/userDataStream'
    security_type = 'USER_STREAM'


# Close a ListenKey:
class close_listenKey_margin:
    params = {'R':['listenKey']}
    method = 'DELETE'
    endpoint = '/sapi/v1/userDataStream'
    security_type = 'USER_STREAM'


### ISOLATED MARGIN ENDPOINTS ###

# Create a ListenKey:
class get_listenKey_isolatedMargin:
    params = None
    method = 'POST'
    endpoint = '/sapi/v1/userDataStream/isolated'
    security_type = 'USER_STREAM'


# Ping/Keep-alive a ListenKey:
class send_listenKey_keepAlive_isolatedMargin:
    params = {'R':['symbol', 'listenKey']}
    method = 'PUT'
    endpoint = '/sapi/v1/userDataStream/isolated'
    security_type = 'USER_STREAM'


# Close a ListenKey:
class close_listenKey_isolatedMargin:
    params = {'R':['symbol', 'listenKey']}
    method = 'DELETE'
    endpoint = '/sapi/v1/userDataStream/isolated'
    security_type = 'USER_STREAM'