'''
Endpoints are collected from the BSwap Endpoints api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#bswap-endpoints
'''

# List All Swap Pools:
class get_swap_pools:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/bswap/pools'
    security_type = 'MARKET_DATA'


# Get liquidity information of a pool:
class get_liquidity_poolInfo:
    params = {'O':['poolId']}
    method = 'GET'
    endpoint = '/sapi/v1/bswap/liquidity'
    security_type = 'USER_DATA'


# Add Liquidity:
class add_liquidity:
    params = {'R':['poolId', 'asset', 'quantity']}
    method = 'POST'
    endpoint = '/sapi/v1/bswap/liquidityAdd'
    security_type = 'TRADE'


# Remove Liquidity:
class remove_liquidity:
    params = {'R':['poolId', 'type', 'asset', 'shareAmount']}
    method = 'POST'
    endpoint = '/sapi/v1/bswap/liquidityRemove'
    security_type = 'TRADE'


# Get Liquidity Operation Record:
class get_liquidity_record:
    params = {'O':['operationId', 'poolId', 'operation', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/bswap/liquidityOps'
    security_type = 'USER_DATA'


# Request Quote:
class get_quote:
    params = {'R':['quoteAsset', 'baseAsset', 'quoteQty']}
    method = 'GET'
    endpoint = '/sapi/v1/bswap/quote'
    security_type = 'USER_DATA'


# Swap:
class make_swap:
    params = {'R':['quoteAsset', 'baseAsset', 'quoteQty']}
    method = 'POST'
    endpoint = '/sapi/v1/bswap/swap'
    security_type = 'TRADE'


# Get Swap History :
class get_swap_history:
    params = {'O':['swapId', 'startTime', 'endTime', 'status', 'quoteAsset', 'baseAsset', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/bswap/swap'
    security_type = 'USER_DATA'
