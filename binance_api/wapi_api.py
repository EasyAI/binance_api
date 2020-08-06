class make_withdraw:
    params = {'R':['asset', 'address', 'amount'],
    'O':['network', 'addressTag', 'name']}
    method = 'POST'
    endpoint = '/wapi/v3/withdraw.html'
    security_type = 'USER_DATA'


class get_deposit_history:
    params = {'O':['asset', 'status', 'startTime', 'endTime']}
    method = 'GET'
    endpoint = '/wapi/v3/depositHistory.html'
    security_type = 'USER_DATA'


class get_withdraw_history:
    params = {'O':['asset', 'status', 'startTime', 'endTime']}
    method = 'GET'
    endpoint = '/wapi/v3/withdrawHistory.html'
    security_type = 'USER_DATA'


class get_deposit_Address:
    params = {'R':['asset'],
        'O':['status']}
    method = 'GET'
    endpoint = '/wapi/v3/depositAddress.html'
    security_type = 'USER_DATA'


class get_account_status:
    params = None
    method = 'GET'
    endpoint = '/wapi/v3/accountStatus.html'
    security_type = 'USER_DATA'


class get_system_status:
    params = None
    method = 'GET'
    endpoint = '/wapi/v3/systemStatus.html'
    security_type = 'NONE'


class get_account_api_trading_status:
    params = None
    method = 'GET'
    endpoint = '/wapi/v3/apiTradingStatus.html'
    security_type = 'USER_DATA'


class get_dustLog:
    params = None
    method = 'GET'
    endpoint = '/wapi/v3/userAssetDribbletLog.html'
    security_type = 'USER_DATA'


class get_tradeFee:
    params = {'O':['symbol']}
    method = 'GET'
    endpoint = '/wapi/v3/tradeFee.html'
    security_type = 'USER_DATA'


class get_assetDetails:
    params = None
    method = 'GET'
    endpoint = '/wapi/v3/assetDetail.html'
    security_type = 'USER_DATA'


class get_subAccounts:
    params = {'O':['email', 'status', 'page', 'limit']}
    method = 'GET'
    endpoint = '/wapi/v3/withdraw.html'
    security_type = 'USER_DATA'


class get_subAccounts_transfers:
    params = {'R':['email'],
    'O':['startTime', 'endTime', 'page', 'limit']}
    method = 'GET'
    endpoint = '/wapi/v3/sub-account/list.html'
    security_type = 'USER_DATA'


class make_subAccounts_transfer:
    params = {'R':['fromEmail', 'toEmail', 'asset', 'amount']}
    method = 'POST'
    endpoint = '/wapi/v3/sub-account/transfer/history.html'
    security_type = 'USER_DATA'


class get_subAccounts_assets:
    params = {'R':['email'],
    'O':['symbol']}
    method = 'GET'
    endpoint = '/wapi/v3/sub-account/assets.html'
    security_type = 'USER_DATA'


class dust_transfer:
    params = {'R':['asset']}
    method = 'POST'
    endpoint = '/sapi/v1/asset/dust'
    security_type = 'USER_DATA'


class get_assetDividendRecord:
    params = {'O':['asset', 'startTime', 'endTime']}
    method = 'GET'
    endpoint = '/sapi/v1/asset/assetDividend'
    security_type = 'USER_DATA'