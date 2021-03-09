'''
Endpoints are collected from the Futures Endpoint api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#futures
'''

# New Future Account Transfer:
class futures_transfer:
    params = {'R':['asset', 'amount', 'type']}
    method = 'POST'
    endpoint = '/sapi/v1/futures/transfer'
    security_type = 'USER_DATA'


# Get Future Account Transaction History List :
class get_futures_transactions:
    params = {'R':['asset', 'startTime'],
            'O':['endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/transfer'
    security_type = 'USER_DATA'


# Borrow For Cross-Collateral:
class borrow_crossCollat:
    params = {'R':['coin', 'amount', 'collateralCoin', 'collateralAmount']}
    method = 'POST'
    endpoint = '/sapi/v1/futures/loan/borrow'
    security_type = 'TRADE'


# Cross-Collateral Borrow History:
class get_crossCollat_borrowHist:
    params = {'O':['coin', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/borrow/history'
    security_type = 'USER_DATA'


# Repay For Cross-Collateral:
class repay_crossCollat:
    params = {'R':['coin', 'collateralCoin', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/futures/loan/repay'
    security_type = 'USER_DATA'


# Cross-Collateral Repayment History:
class get_crossCollat_repayHist:
    params = {'R':['coin', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/repay/history'
    security_type = 'USER_DATA'


# Cross-Collateral Wallet:
class get_crossCollat_wallet:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/wallet'
    security_type = 'USER_DATA'


# Cross-Collateral Wallet V2:
class get_crossCollat_wallet_v2:
    params = None
    method = 'GET'
    endpoint = '/sapi/v2/futures/loan/wallet'
    security_type = 'USER_DATA'


# Cross-Collateral Information:
class get_crossCollat_info:
    params = {'O':['collateralCoin']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/configs'
    security_type = 'USER_DATA'


# Cross-Collateral Information V2:
class get_crossCollat_info_v2:
    params = {'O':['loanCoin', 'collateralCoin']}
    method = 'GET'
    endpoint = '/sapi/v2/futures/loan/configs'
    security_type = 'USER_DATA'


# Calculate Rate After Adjust Cross-Collateral LTV:
class get_crossCollat_rate_LTV:
    params = {'R':['collateralCoin', 'amount', 'direction']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/calcAdjustLevel'
    security_type = 'USER_DATA'


# Calculate Rate After Adjust Cross-Collateral LTV V2:
class get_crossCollat_rate_LTV_v2:
    params = {'R':['loanCoin', 'collateralCoin', 'amount', 'direction']}
    method = 'GET'
    endpoint = '/sapi/v2/futures/loan/calcAdjustLevel'
    security_type = 'USER_DATA'


# Get Max Amount for Adjust Cross-Collateral LTV:
class get_crossCollat_max_LTV:
    params = {'R':['collateralCoin']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/calcMaxAdjustAmount'
    security_type = 'USER_DATA'


# Get Max Amount for Adjust Cross-Collateral LTV V2:
class get_crossCollat_max_LTV_v2:
    params = {'R':['loanCoin', 'collateralCoin']}
    method = 'GET'
    endpoint = '/sapi/v2/futures/loan/calcMaxAdjustAmount'
    security_type = 'USER_DATA'


# Adjust Cross-Collateral LTV:
class adjust_crossCollat_LTV:
    params = {'R':['collateralCoin', 'amount', 'direction']}
    method = 'POST'
    endpoint = '/sapi/v1/futures/loan/adjustCollateral'
    security_type = 'TRADE'


# Adjust Cross-Collateral LTV V2:
class adjust_crossCollat_LTV_v2:
    params = {'R':['loanCoin', 'collateralCoin', 'amount', 'direction']}
    method = 'POST'
    endpoint = '/sapi/v2/futures/loan/adjustCollateral'
    security_type = 'TRADE'


# Adjust Cross-Collateral LTV History:
class adjust_crossCollat_LTV_history:
    params = {'O':['loanCoin', 'collateralCoin', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/adjustCollateral/history'
    security_type = 'USER_DATA'


# Cross-Collateral Liquidation History:
class adjust_crossCollat_liquidation_history:
    params = {'O':['loanCoin', 'collateralCoin', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/liquidationHistory'
    security_type = 'USER_DATA'


# Check Collateral Repay Limit:
class get_collatRepay_limit:
    params = {'R':['coin', 'collateralCoin']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/collateralRepayLimit'
    security_type = 'USER_DATA'


# Get Collateral Repay Quote:
class get_collatRepay_quote:
    params = {'R':['coin', 'collateralCoin', 'amount']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/collateralRepay'
    security_type = 'USER_DATA'


# Repay with Collateral:
class collateral_repay:
    params = {'R':['quoteId']}
    method = 'POST'
    endpoint = '/sapi/v1/futures/loan/collateralRepay'
    security_type = 'USER_DATA'


# Collateral Repayment Result:
class get_collatRepay_result:
    params = {'R':['quoteId']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/collateralRepayResult'
    security_type = 'USER_DATA'


# Cross-Collateral Interest History:
class get_crossCollat_interestHist:
    params = {'O':['collateralCoin', 'startTime', 'endTime', 'current', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/interestHistory'
    security_type = 'USER_DATA'