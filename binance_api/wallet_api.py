'''
Endpoints are collected from the Wallet Endpoints api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#wallet-endpoints
'''

# System Status:
class make_withdraw:
    params = None
    method = 'GET'
    endpoint = '/wapi/v3/systemStatus.html'
    security_type = 'System'


# All Coins' Information:
class make_withdraw:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/capital/config/getall'
    security_type = 'USER_DATA'


#Daily Account Snapshot:
class make_withdraw:
    params = {'R':['type'],
            'O':['startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/accountSnapshot'
    security_type = 'USER_DATA'


# Disable Fast Withdraw Switch:
class make_withdraw:
    params = None
    method = 'POST'
    endpoint = '/sapi/v1/account/disableFastWithdrawSwitch'
    security_type = 'USER_DATA'


# Enable Fast Withdraw Switch:
class make_withdraw:
    params = None
    method = 'POST'
    endpoint = '/sapi/v1/account/enableFastWithdrawSwitch'
    security_type = 'USER_DATA'


# Withdraw [SAPI]:
class make_withdraw:
    params = {'R':['coin', 'address', 'amount'],
            'O':['withdrawOrderId', 'network', 'addressTag', 'transactionFeeFlag', 'name']}
    method = 'POST'
    endpoint = '/sapi/v1/capital/withdraw/apply'
    security_type = 'USER_DATA'


# Withdraw:
class make_withdraw:
    params = {'R':['asset', 'address', 'amount'],
            'O':['withdrawOrderId', 'network', 'addressTag', 'transactionFeeFlag', 'name']}
    method = 'POST'
    endpoint = '/wapi/v3/withdraw.html'
    security_type = 'USER_DATA'


# Deposit History(supporting network):
class make_withdraw:
    params = {'O':['coin', 'status', 'startTime', 'endTime', 'offest', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/capital/deposit/hisrec'
    security_type = 'USER_DATA'


# Deposit History:
class make_withdraw:
    params = {'O':['asset', 'status', 'startTime', 'endTime']}
    method = 'GET'
    endpoint = '/wapi/v3/depositHistory.html'
    security_type = 'USER_DATA'


# Withdraw History (supporting network):
class make_withdraw:
    params = {'O':['coin', 'status', 'offset', 'limit', 'startTime', 'endTime']}
    method = 'GET'
    endpoint = '/sapi/v1/capital/withdraw/history'
    security_type = 'USER_DATA'


# Withdraw History:
class make_withdraw:
    params = {'O':['asset', 'status', 'startTime', 'endTime']}
    method = 'GET'
    endpoint = '/wapi/v3/withdrawHistory.html'
    security_type = 'USER_DATA'


# Deposit Address (supporting network):
class make_withdraw:
    params = {'R':['coin'],
            'O':['network']}
    method = 'GET'
    endpoint = '/sapi/v1/capital/deposit/address'
    security_type = 'USER_DATA'


# Deposit Address:
class make_withdraw:
    params = {'R':['asset'],
            'O':['status']}
    method = 'GET'
    endpoint = '/wapi/v3/depositAddress.html'
    security_type = 'USER_DATA'


# Account Status:
class make_withdraw:
    params = None
    method = 'GET'
    endpoint = '/wapi/v3/accountStatus.html'
    security_type = 'USER_DATA'


# Account API Trading Status:
class make_withdraw:
    params = None
    method = 'GET'
    endpoint = '/wapi/v3/apiTradingStatus.html'
    security_type = 'USER_DATA'


# DustLog:
class make_withdraw:
    params = None
    method = 'GET'
    endpoint = '/wapi/v3/userAssetDribbletLog.html'
    security_type = 'USER_DATA'


# Dust Transfer:
class make_withdraw:
    params = {'R':['asset']}
    method = 'POST'
    endpoint = '/sapi/v1/asset/dust'
    security_type = 'USER_DATA'


# Asset Dividend Record:
class make_withdraw:
    params = {'O':['asset', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/asset/assetDividend'
    security_type = 'USER_DATA'


# Asset Detail:
class make_withdraw:
    params = None
    method = 'GET'
    endpoint = '/wapi/v3/assetDetail.html'
    security_type = 'USER_DATA'


# Trade Fee:
class make_withdraw:
    params = {'O':['symbol']}
    method = 'GET'
    endpoint = '/wapi/v3/tradeFee.html'
    security_type = 'USER_DATA'


# User Universal Transfer:
class make_withdraw:
    params = {'R':['type', 'asset', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/asset/transfer'
    security_type = 'USER_DATA'


# Query User Universal Transfer History
class make_withdraw:
    params = {'R':['type'],
        'O':['startTime', 'endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/asset/transfer'
    security_type = 'USER_DATA'