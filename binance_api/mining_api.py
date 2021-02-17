'''
Endpoints are collected from the Mining Endpoints api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#mining-endpoints
'''

# Acquiring Algorithm:
class get_algorithm:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/mining/pub/algoList'
    security_type = 'USER_DATA'


# Acquiring CoinName:
class get_coinNames:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/mining/pub/coinList'
    security_type = 'USER_DATA'


# Request for Detail Miner List:
class get_minerList_detail:
    params = {'R':['algo', 'userName', 'workerName']}
    method = 'GET'
    endpoint = '/sapi/v1/mining/worker/detail'
    security_type = 'USER_DATA'


# Request for Miner List:
class get_minerList:
    params = {'R':['algo', 'userName'],
            'O':['pageIndex', 'sort', 'sortColumn', 'worderStatus']}
    method = 'GET'
    endpoint = '/sapi/v1/mining/worker/list'
    security_type = 'USER_DATA'


# Earnings List:
class get_earningsList:
    params = {'R':['algo', 'userName'],
            'O':['coin', 'startDate', 'endDate', 'pageIndex', 'pageSize']}
    method = 'GET'
    endpoint = '/sapi/v1/mining/payment/list'
    security_type = 'USER_DATA'


# Extra Bonus List:
class get_extraBonusList:
    params = {'R':['algo', 'userName'],
            'O':['coin', 'startDate', 'endDate', 'pageIndex', 'pageSize']}
    method = 'GET'
    endpoint = '/sapi/v1/mining/payment/other'
    security_type = 'USER_DATA'


# Hashrate Resale List:
class get_hashrateResaleList:
    params = {'O':['pageIndex', 'pageSize']}
    method = 'GET'
    endpoint = '/sapi/v1/mining/hash-transfer/config/details/list'
    security_type = 'USER_DATA'


# Hashrate Resale Detail:
class get_hashrateResaleDetail:
    params = {'R':['configId', 'userName'],
            'O':['pageIndex', 'pageSize']}
    method = 'GET'
    endpoint = '/sapi/v1/mining/hash-transfer/profit/details'
    security_type = 'USER_DATA'


# Hashrate Resale Request:
class post_hashrateResale:
    params = {'R':['userName', 'algo', 'endDate', 'startDate', 'toPoolUser', 'hashRate']}
    method = 'POST'
    endpoint = '/sapi/v1/mining/hash-transfer/config'
    security_type = 'USER_DATA'


# Cancel hashrate resale configuration:
class cancel_hashrateResale:
    params = {'R':['configId', 'userName']}
    method = 'POST'
    endpoint = '/sapi/v1/mining/hash-transfer/config/cancel'
    security_type = 'USER_DATA'


# Statistic List:
class get_statisticList:
    params = {'R':['algo', 'userName']}
    method = 'GET'
    endpoint = '/sapi/v1/mining/statistics/user/status'
    security_type = 'USER_DATA'


# Account List:
class get_accountList:
    params = {'R':['algo', 'userName']}
    method = 'GET'
    endpoint = '/sapi/v1/mining/statistics/user/list'
    security_type = 'USER_DATA'