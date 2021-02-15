'''
Endpoints are collected from the Saving Endpoints api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#savings-endpoints
'''

# Get Flexible Product List:
class get_:
    params = {'O':['status', 'featured']}
    method = 'GET'
    endpoint = '/sapi/v1/lending/daily/product/list'
    security_type = 'USER_DATA'


# Get Left Daily Purchase Quota of Flexible Product:
class place_order:
    params = {'R':['productId']}
    method = 'GET'
    endpoint = '/sapi/v1/lending/daily/userLeftQuota'
    security_type = 'USER_DATA'


# Purchase Flexible Product:
class place_order:
    params = {'R':['productId', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/lending/daily/purchase'
    security_type = 'USER_DATA'


# Get Left Daily Redemption Quota of Flexible Product:
class place_order:
    params = {'R':['productId', 'type']}
    method = 'GET'
    endpoint = '/sapi/v1/lending/daily/userRedemptionQuota'
    security_type = 'USER_DATA'


# Redeem Flexible Product
class place_order:
    params = {'R':['productId', 'amount', 'type']}
    method = 'POST'
    endpoint = '/sapi/v1/lending/daily/redeem'
    security_type = 'USER_DATA'


# Get Flexible Product Position:
class place_order:
    params = {'R':['asset']}
    method = 'GET'
    endpoint = '/sapi/v1/lending/daily/token/position'
    security_type = 'USER_DATA'


# Get Fixed and Activity Project List:
class place_order:
    params = {'R':['type'],
            'O':['asset', 'status', 'isSortAsc', 'sortBy', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/lending/project/list'
    security_type = 'USER_DATA'


# Purchase Fixed/Activity Project:
class place_order:
    params = {'R':['projectId', 'lot']}
    method = 'POST'
    endpoint = '/sapi/v1/lending/customizedFixed/purchase'
    security_type = 'USER_DATA'


# Get Fixed/Activity Project Position:
class place_order:
    params = {'R':['asset'],
            'O':['projectId', 'status']}
    method = 'GET'
    endpoint = '/sapi/v1/lending/project/position/list'
    security_type = 'USER_DATA'


# Lending Account:
class place_order:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/lending/union/account'
    security_type = 'USER_DATA'


# Get Purchase Record:
class place_order:
    params = {'R':['lendingType'],
            'O':['asset', 'startTime', 'endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/lending/union/purchaseRecord'
    security_type = 'USER_DATA'


# Get Redemption Record:
class place_order:
    params = {'R':['lendingType'],
            'O':['asset', 'startTime', 'endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/lending/union/redemptionRecord'
    security_type = 'USER_DATA'


# Get Interest History:
class place_order:
    params = {'R':['lendingType'],
            'O':['asset', 'startTime', 'endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/lending/union/interestHistory'
    security_type = 'USER_DATA'


# Change Fixed/Activity Position to Daily Position:
class place_order:
    params = {'R':['productId', 'lot', 'positionId']}
    method = 'POST'
    endpoint = '/sapi/v1/lending/positionChanged'
    security_type = 'USER_DATA'