'''
Endpoints are collected from the Sub-Account Endpoints api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#sub-account-endpoints
'''

# Query Sub-account List (For Master Account):
class get_subAccount_list:
    params = {'O':['email', 'status', 'page', 'limit']}
    method = 'GET'
    endpoint = '/wapi/v3/sub-account/list.html'
    security_type = 'NONE'


# Query Sub-account Spot Asset Transfer History (For Master Account):
class get_subAccount_spotTransferHistory_wapi:
    params = {'R':['email'],
            'O':['startTime', 'endTime', 'page', 'limit']}
    method = 'GET'
    endpoint = '/wapi/v3/sub-account/transfer/history.html'
    security_type = 'NONE'


# Query Sub-account Spot Asset Transfer History (SAPI For Master Account):
class get_subAccount_spotTransferHistory_sapi:
    params = {'O':['fromEmail', 'toEmail', 'startTime', 'endTime', 'page', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/sub/transfer/history'
    security_type = 'USER_DATA'


# Sub-account Spot Asset Transfer (For Master Account):
class subAccount_spotAsset_transfer:
    params = {'R':['fromEmail', 'toEmail', 'asset', 'amount']}
    method = 'POST'
    endpoint = '/wapi/v3/sub-account/transfer.html'
    security_type = 'NONE'


# Query Sub-account Futures Asset Transfer History (For Master Account):
class get_subAccount_futuresTransferHistory:
    params = {'R':['email', 'futuresType'],
            'O':['startTime', 'endTime', 'page', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/futures/internalTransfer'
    security_type = 'USER_DATA'


# Sub-account Futures Asset Transfer (For Master Account):
class subAccount_futuresAsset_transfer:
    params = {'R':['fromEmail', 'toEmail', 'futuresType', 'asset', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/sub-account/futures/internalTransfer'
    security_type = 'USER_DATA'


# Query Sub-account Assets (For Master Account):
class get_subAccount_assets:
    params = {'R':['email']}
    method = 'GET'
    endpoint = '/wapi/v3/sub-account/assets.html'
    security_type = 'NONE'


# Query Sub-account Spot Assets Summary (For Master Account):
class get_subAccount_spotAssetsSummary:
    params = {'O':['email', 'page', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/spotSummary'
    security_type = 'USER_DATA'


# Get Sub-account Deposit Address (For Master Account):
class get_subAccount_depositAddress:
    params = {'R':['email', 'coin'],
            'O':['network']}
    method = 'GET'
    endpoint = '/sapi/v1/capital/deposit/subAddress'
    security_type = 'USER_DATA'


# Get Sub-account Deposit History (For Master Account):
class get_subAccount_depositHistory:
    params = {'R':['email'],
            'O':['coin', 'status', 'startTime', 'endTime', 'limit', 'offset']}
    method = 'GET'
    endpoint = '/sapi/v1/capital/deposit/subHisrec'
    security_type = 'USER_DATA'


# Get Sub-account's Status on Margin/Futures (For Master Account):
class get_subAccount_statusFnM:
    params = {'O':['email']}
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/status'
    security_type = 'USER_DATA'


# Enable Margin for Sub-account (For Master Account):
class enable_subAccount_margin:
    params = {'R':['email']}
    method = 'POST'
    endpoint = '/sapi/v1/sub-account/margin/enable'
    security_type = 'USER_DATA'


# Get Detail on Sub-account's Margin Account (For Master Account):
class get_subAccount_marginAccount:
    params = {'R':['email']}
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/margin/account'
    security_type = 'USER_DATA'


# Get Summary of Sub-account's Margin Account (For Master Account):
class get_subAccount_marginAccountSummary:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/margin/accountSummary'
    security_type = 'USER_DATA'


# Enable Futures for Sub-account (For Master Account):
class enable_subAccount_futures:
    params = {'R':['email']}
    method = 'POST'
    endpoint = '/sapi/v1/sub-account/futures/enable'
    security_type = 'USER_DATA'


# Get Detail on Sub-account's Futures Account (For Master Account):
class get_subAccount_futuresAccount:
    params = {'R':['email']}
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/futures/account'
    security_type = 'USER_DATA'


# Get Summary of Sub-account's Futures Account (For Master Account):
class get_subAccount_futuresAccountSummary:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/futures/accountSummary'
    security_type = 'USER_DATA'


# Get Futures Position-Risk of Sub-account (For Master Account)
class get_subAccount_positionRisk:
    params = {'R':['email']}
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/futures/positionRisk'
    security_type = 'USER_DATA'


# Futures Transfer for Sub-account (For Master Account):
class subAccount_futures_transfer:
    params = {'R':['email', 'asset']}
    method = 'POST'
    endpoint = '/sapi/v1/sub-account/futures/transfer'
    security_type = 'USER_DATA'


# Margin Transfer for Sub-account (For Master Account):
class subAccount_margin_transfer:
    params = {'R':['email', 'asset', 'amount', 'type']}
    method = 'POST'
    endpoint = '/sapi/v1/sub-account/margin/transfer'
    security_type = 'USER_DATA'


# Transfer to Sub-account of Same Master (For Sub-account):
class master_sub_transfer:
    params = {'R':['toEmail', 'asset', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/sub-account/transfer/subToSub'
    security_type = 'USER_DATA'


# Transfer to Master (For Sub-account):
class sub_master_transfer:
    params = {'R':['asset', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/sub-account/transfer/subToMaster'
    security_type = 'USER_DATA'


# Sub-account Transfer History (For Sub-account)
class get_subAccount_transferHistory:
    params = {'O':['asset', 'type', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/transfer/subUserHistory'
    security_type = 'USER_DATA'


# Universal Transfer (For Master Account):
class make_universalTransfer:
    params = {'R':['fromAccountType', 'toAccountType', 'asset', 'amount'],
            'O':['toEmail', 'fromEmail']}
    method = 'POST'
    endpoint = '/sapi/v1/sub-account/universalTransfer'
    security_type = 'NONE'


# Query Universal Transfer History:
class get_universalTransferHisotry:
    params = {'O':['fromEmail', 'toEmail', 'startTime', 'endTime', 'page', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/sub-account/universalTransfer'
    security_type = 'USER_DATA'


# Get Detail on Sub-account's Futures Account V2 (For Master Account):
class get_subAccount_futuresAccount_v2:
    params = {'R':['email', 'futuresType']}
    method = 'GET'
    endpoint = '/sapi/v2/sub-account/futures/account'
    security_type = 'USER_DATA'


# Get Summary of Sub-account's Futures Account V2 (For Master Account):
class get_subAccount_futuresAccountSummary_v2:
    params = {'R':['futuresType'],
            'O':['page', 'type']}
    method = 'GET'
    endpoint = '/sapi/v2/sub-account/futures/accountSummary'
    security_type = 'USER_DATA'


# Get Futures Position-Risk of Sub-account V2 (For Master Account):
class get_subAccount_positionRisk_v2:
    params = {'R':['email', 'futuresType']}
    method = 'GET'
    endpoint = '/sapi/v2/sub-account/futures/positionRisk'
    security_type = 'USER_DATA'