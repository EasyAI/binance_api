#! /usr/bin/env python3

import hmac
import time
import json
import logging
import requests
from hashlib import sha256
from urllib.parse import urlencode

from . import formatter
from . import custom_data_formatter

## API Object imports
from . import blvt_api
from . import bswap_api
from . import futures_api
from . import margin_api
from . import marketData_api
from . import mining_api
from . import savings_api
from . import spot_api
from . import subAccount_api
from . import userDataStream_api
from . import wallet_api


## sets up the rest BASE for binances rest API.
REST_BASE = 'https://api.binance.com'

NO_REQUIREMENTS = ['NONE']
REQUIRE_KEY = ['MARKET_DATA', 'USER_STREAM']
REQUIRE_SIGNATURE = ['USER_DATA', 'TRADE', 'MARGIN']

class Binance_REST:

    def __init__(self, public_key=None, private_key=None, default_api_type=None):
        self.requests_made  = 0
        self.errors         = 0

        self.default_api_type   = default_api_type
        self.public_key         = public_key
        self.private_key        = private_key


    ## ------------------ [BLVT_EXCLUSIVE] ------------------ ##
    def get_blvt_info(self, **kwargs):
        return()
    def subscribe_blvt(self, **kwargs):
        return()
    def query_subscription_record(self, **kwargs):
        return()
    def redeem_blvt(self, **kwargs):
        return()
    def query_redemption_record(self, **kwargs):
        return()
    def get_blvt_userLimit(self, **kwargs):
        return()

    ## ------------------ [BSWAP_EXCLUSIVE] ------------------ ##
    def get_swap_pools(self):
        return()
    def get_liquidity_poolInfo(self, **kwargs):
        return()
    def add_liquidity(self, **kwargs):
        return()
    def remove_liquidity(self, **kwargs):
        return()
    def get_liquidity_record(self, **kwargs):
        return()
    def get_quote(self, **kwargs):
        return()
    def make_swap(self, **kwargs):
        return()
    def get_swap_history(self, **kwargs):
        return()

    ## ------------------ [FUTURES_EXCLUSIVE] ------------------ ##
    def futures_transfer(self, **kwargs):
        return()
    def get_futures_transactions(self, **kwargs):
        return()
    def borrow_crossCollat(self, **kwargs):
        return()
    def get_crossCollat_borrowHist(self, **kwargs):
        return()
    def repay_crossCollat(self, **kwargs):
        return()
    def get_crossCollat_repayHist(self, **kwargs):
        return()
    def get_crossCollat_wallet(self):
        return()
    def get_crossCollat_wallet_v2(self):
        return()
    def get_crossCollat_info(self, **kwargs):
        return()
    def get_crossCollat_info_v2(self, **kwargs):
        return()
    def get_crossCollat_rate_LTV(self, **kwargs):
        return()
    def get_crossCollat_rate_LTV_v2(self, **kwargs):
        return()
    def get_crossCollat_max_LTV(self, **kwargs):
        return()
    def get_crossCollat_max_LTV_v2(self, **kwargs):
        return()
    def adjust_crossCollat_LTV(self, **kwargs):
        return()
    def adjust_crossCollat_LTV_v2(self, **kwargs):
        return()
    def adjust_crossCollat_LTV_history(self, **kwargs):
        return()
    def adjust_crossCollat_liquidation_history(self, **kwargs):
        return()
    def get_collatRepay_limit(self, **kwargs):
        return()
    def get_collatRepay_quote(self, **kwargs):
        return()
    def collateral_repay(self, **kwargs):
        return()
    def get_collatRepay_result(self, **kwargs):
        return()
    def get_crossCollat_interestHist(self, **kwargs):
        return()

    ## ------------------ [MARGIN_EXCLUSIVE] ------------------ ##
    def margin_transfer(self, **kwargs):
        return()
    def margin_accountBorrow(self, **kwargs):
        return()
    def margin_accountRepay(self, **kwargs):
        return()
    def query_margin_asset(self, **kwargs):
        return()
    def query_crossPair(self, **kwargs):
        return()
    def get_margin_allAssets(self):
        return()
    def get_allCrossPairs(self):
        return()
    def query_margin_priceIndex(self, **kwargs):
        return()
    def place_order(self, **kwargs):
        return()
    def cancel_order(self, **kwargs):
        return()
    def cancel_all_orders(self, **kwargs):
        return()
    def get_margin_crossTransferHistory(self, **kwargs):
        return()
    def get_loanRecord(self, **kwargs):
        return()
    def get_repayRecord(self, **kwargs):
        return()
    def get_interestHistory(self, **kwargs):
        return()
    def get_fLiquidationRecord(self, **kwargs):
        return()
    def get_cross_accountDetails(self):
        return()
    def get_orders(self, **kwargs):
        return()
    def get_open_orders(self, **kwargs):
        return()
    def get_all_orders(self, **kwargs):
        return()
    def get_all_trades(self, **kwargs):
        return()
    def get_maxBorrow(self, **kwargs):
        return()
    def get_maxOutAmmount(self, **kwargs):
        return()
    def create_isolatedMaringAccount(self, **kwargs):
        return()
    def isolated_transfer(self, **kwargs):
        return()
    def get_isolated_transferHistory(self, **kwargs):
        return()
    def get_isolated_accountInfo(self, **kwargs):
        return()
    def get_isolated_symbol(self, **kwargs):
        return()
    def get_isolated_symbol_all(self):
        return()
    def toggle_BNB_burn_ST_MI(self, **kwargs):
        return()
    def get_BNB_burn_status(self):
        return()

    ## ------------------ [MARKET_DATA_EXCLUSIVE] ------------------ ##
    def test_ping(self):
        return()
    def get_serverTime(self):
        return()
    def get_ExchangeInfo(self):
        return()
    def get_orderBook(self, **kwargs):
        return()
    def get_recentTrades(self, **kwargs):
        return()
    def get_oldTrades(self, **kwargs):
        return()
    def get_aggTradeList(self, **kwargs):
        return()
    def get_candles(self, **kwargs):
        return()
    def get_averagePrice(self, **kwargs):
        return()
    def get_24hTicker(self, **kwargs):
        return()
    def get_priceTicker(self, **kwargs):
        return()
    def get_orderbookTicker(self, **kwargs):
        return()

    ## ------------------ [MINING_EXCLUSIVE] ------------------ ##
    def get_algorithm(self):
        return()
    def get_coinNames(self):
        return()
    def get_minerList_detail(self, **kwargs):
        return()
    def get_minerList(self, **kwargs):
        return()
    def get_earningsList(self, **kwargs):
        return()
    def get_extraBonusList(self, **kwargs):
        return()
    def get_hashrateResaleList(self, **kwargs):
        return()
    def get_hashrateResaleDetail(self, **kwargs):
        return()
    def post_hashrateResale(self, **kwargs):
        return()
    def cancel_hashrateResale(self, **kwargs):
        return()
    def get_statisticList(self, **kwargs):
        return()
    def get_accountList(self, **kwargs):
        return()

    ## ------------------ [SAVINGS_EXCLUSIVE] ------------------ ##
    def get_productList(self, **kwargs):
        return()
    def get_dailyPurchaseQuota(self, **kwargs):
        return()
    def purchase_product(self, **kwargs):
        return()
    def get_dailyRedemptionQuota(self, **kwargs):
        return()
    def redeem_product(self, **kwargs):
        return()
    def get_product_position(self, **kwargs):
        return()
    def get_FnAProject_list(self, **kwargs):
        return()
    def purchase_FnAProject(self, **kwargs):
        return()
    def get_FnAProject_position(self, **kwargs):
        return()
    def get_lending(self):
        return()
    def get_purchase_record(self, **kwargs):
        return()
    def get_redemption_record(self, **kwargs):
        return()
    def get_interest_history(self, **kwargs):
        return()
    def change_position(self, **kwargs):
        return()

    ## ------------------ [SPOT_EXCLUSIVE] ------------------ ##
    def place_order_test(self, **kwargs):
        return()
    def place_order(self, **kwargs):
        return()
    def cancel_order(self, **kwargs):
        return()
    def cancel_all_orders(self, **kwargs):
        return()
    def query_order(self, **kwargs):
        return()
    def get_openOrders(self, **kwargs):
        return()
    def get_allOrders(self, **kwargs):
        return()
    def place_order_oco(self, **kwargs):
        return()
    def cancel_order_oco(self, **kwargs):
        return()
    def query_order_oco(self, **kwargs):
        return()
    def get_allOrders_oco(self, **kwargs):
        return()
    def get_openOrders_oco(self):
        return()
    def get_accountInfo(self):
        return()
    def get_tradeList(self, **kwargs):
        return()

    ## ------------------ [SUB-ACCOUNT_EXCLUSIVE] ------------------ ##
    def get_subAccount_list(self, **kwargs):
        return()
    def get_subAccount_spotTransferHistory_wapi(self, **kwargs):
        return()
    def get_subAccount_spotTransferHistory_sapi(self, **kwargs):
        return()
    def subAccount_spotAsset_transfer(self, **kwargs):
        return()
    def get_subAccount_futuresTransferHistory(self, **kwargs):
        return()
    def subAccount_futuresAsset_transfer(self, **kwargs):
        return()
    def get_subAccount_assets(self, **kwargs):
        return()
    def get_subAccount_spotAssetsSummary(self, **kwargs):
        return()
    def get_subAccount_depositAddress(self, **kwargs):
        return()
    def get_subAccount_depositHistory(self, **kwargs):
        return()
    def get_subAccount_statusFnM(self, **kwargs):
        return()
    def enable_subAccount_margin(self, **kwargs):
        return()
    def get_subAccount_marginAccount(self, **kwargs):
        return()
    def get_subAccount_marginAccountSummary(self):
        return()
    def enable_subAccount_futures(self, **kwargs):
        return()
    def get_subAccount_futuresAccount(self, **kwargs):
        return()
    def get_subAccount_futuresAccountSummary(self):
        return()
    def get_subAccount_positionRisk(self, **kwargs):
        return()
    def subAccount_futures_transfer(self, **kwargs):
        return()
    def subAccount_margin_transfer(self, **kwargs):
        return()
    def master_sub_transfer(self, **kwargs):
        return()
    def sub_master_transfer(self, **kwargs):
        return()
    def get_subAccount_transferHistory(self, **kwargs):
        return()
    def make_universalTransfer(self, **kwargs):
        return()
    def get_universalTransferHisotry(self, **kwargs):
        return()
    def get_subAccount_futuresAccount_v2(self, **kwargs):
        return()
    def get_subAccount_futuresAccountSummary_v2(self, **kwargs):
        return()
    def get_subAccount_positionRisk_v2(self, **kwargs):
        return()

    ## ------------------ [WALLET_EXCLUSIVE] ------------------ ##
    def get_systemStatus(self):
        return()
    def get_allCoinsInfo(self):
        return()
    def get_dailySnapshot(self, **kwargs):
        return()
    def disable_withdrawSwitch(self):
        return()
    def enable_withdrawSwitch(self):
        return()
    def make_withdraw_SAPI(self, **kwargs):
        return()
    def make_withdraw(self, **kwargs):
        return()
    def get_depositHistory_SN(self, **kwargs):
        return()
    def get_depositHistory(self, **kwargs):
        return()
    def get_withdrawHistory_SN(self, **kwargs):
        return()
    def get_withdrawHistory(self, **kwargs):
        return()
    def depositAddress_SN(self, **kwargs):
        return()
    def depositAddress(self, **kwargs):
        return()
    def get_accountStatus(self):
        return()
    def get_apiStatus(self):
        return()
    def get_dustLog(self):
        return()
    def make_dustTransfer(self, **kwargs):
        return()
    def get_dividendRecord(self, **kwargs):
        return()
    def get_assetDetail(self):
        return()
    def get_tradeFee(self, **kwargs):
        return()
    def make_universalTransfer(self, **kwargs):
        return()
    def get_universalTransferHistory(self, **kwargs):
        return()

    ## ------------------ [USER_DATA_STREAM_EXCLUSIVE] ------------------ ##
    def get_listenKey(self, api_type=None):
        if api_type == 'SPOT':
            return(self.param_check(userDataStream_api.get_listenKey_spot))
        elif api_type == 'MARGIN':
            return(self.param_check(userDataStream_api.get_listenKey_margin))
        elif api_type == 'FUTURES':
            return(self.param_check(userDataStream_api.send_listenKey_keepAlive_margin, kwargs))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def send_listenKey_keepAlive(self, api_type='SPOT', **kwargs):
        if api_type == 'SPOT':
            return(self.param_check(userDataStream_api.send_listenKey_keepAlive_spot, kwargs))
        elif api_type == 'MARGIN':
            return(self.param_check(userDataStream_api.send_listenKey_keepAlive_margin, kwargs))
        elif api_type == 'FUTURES':
            return(self.param_check(userDataStream_api.send_listenKey_keepAlive_margin, kwargs))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def close_listenKey(self, api_type='SPOT', **kwargs):
        if api_type == 'SPOT':
            return(self.param_check(userDataStream_api.close_listenKey_spot, kwargs))
        elif api_type == 'MARGIN':
            return(self.param_check(userDataStream_api.close_listenKey_margin, kwargs))
        elif api_type == 'FUTURES':
            return(self.param_check(userDataStream_api.send_listenKey_keepAlive_margin, kwargs))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')


    ## ------------------ [MULTI_API_ENDPOINT] ------------------ ##
    def place_order(self, api_type=None, **kwargs):
        if api_type == None:
            api_type = self.default_api_type

        if api_type == 'SPOT':
            return(self.param_check(spot_api.place_order, kwargs))
        elif api_type == 'MARGIN':
            return(self.param_check(margin_api.place_order, kwargs))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def cancel_order(self, api_type=None, **kwargs):
        if api_type == None:
            api_type = self.default_api_type

        if api_type == 'SPOT':
            return(self.param_check(spot_api.cancel_order, kwargs))
        elif api_type == 'MARGIN':
            return(self.param_check(margin_api.cancel_order, kwargs))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def get_account(self, api_type=None):
        if api_type == None:
            api_type = self.default_api_type

        if api_type == 'SPOT':
            return(self.param_check(spot_api.get_account))
        elif api_type == 'MARGIN':
            return(self.param_check(margin_api.get_account))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def get_all_orders(self, api_type=None, **kwargs):
        if api_type == None:
            api_type = self.default_api_type

        if api_type == 'SPOT':
            return(self.param_check(spot_api.get_all_orders, kwargs))
        elif api_type == 'MARGIN':
            return(self.param_check(margin_api.get_all_orders, kwargs))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def get_all_trades(self, api_type=None, **kwargs):
        if api_type == None:
            api_type = self.default_api_type

        if api_type == 'SPOT':
            return(self.param_check(spot_api.get_all_trades, kwargs))
        elif api_type == 'MARGIN':
            return(self.param_check(margin_api.get_all_trades, kwargs))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def get_open_orders(self, api_type=None, **kwargs):
        if api_type == None:
            api_type = self.default_api_type

        if api_type == 'SPOT':
            return(self.param_check(spot_api.get_open_orders, kwargs))
        elif api_type == 'MARGIN':
            return(self.param_check(margin_api.get_open_orders, kwargs))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')


    def param_check(self, api_info, users_passed_parameters=None):
        if api_info.params != None:
            missingParameters = []
            allParams = []

            if 'symbol' in users_passed_parameters:
                if '-' in users_passed_parameters:
                    base, quote = users_passed_parameters['symbol'].split('-')
                    users_passed_parameters.update({'symbol':(quote+base).upper()})

            if 'R' in api_info.params:
                allParams += api_info.params['R']
                for param in api_info.params['R']:
                    if not(param in users_passed_parameters):
                        missingParameters.append(param)

            if len(missingParameters) >= 1:
                return('MISSING_REQUIRED_PARAMETERS', missingParameters)

            if 'O' in api_info.params:
                allParams += api_info.params['O']

            unknownParams = []

            for param in users_passed_parameters:
                if not(param in allParams):
                    unknownParams.append(param)

            if len(unknownParams) >= 1:
                return('UNEXPECTED_PARAMETERS', unknownParams)

            params = users_passed_parameters
        else:
            if users_passed_parameters != None and users_passed_parameters != {}:
                return('ENDPOINT_TAKES_NO_PARAMETERS_BUT_SOME_WHERE_GIVEN', users_passed_parameters)
            params = {}

        req_KEY = False
        req_SIG = False

        if api_info.security_type in REQUIRE_SIGNATURE:
            req_SIG = True

        if api_info.security_type in REQUIRE_KEY or req_SIG:
            req_KEY = True

        return(self.api_request(api_info.method, api_info.endpoint, params, req_KEY, req_SIG))


    def api_request(self, method, path, params, req_KEY, req_SIG):
        params_encoded = urlencode(sorted(params.items()))

        if req_SIG:
            query = '{0}&timestamp={1}'.format(params_encoded, int(time.time()*1000))
            signature = hmac.new(bytes(self.private_key.encode('utf-8')), (query).encode('utf-8'), sha256).hexdigest()
            urlQuery = '{0}{1}?{2}&signature={3}'.format(REST_BASE, path, query, signature)
        else:
            if params_encoded:
                urlQuery = '{0}{1}?{2}'.format(REST_BASE, path, params_encoded)
            else:
                urlQuery = '{0}{1}'.format(REST_BASE, path)

        if req_KEY:
            headers = {'X-MBX-APIKEY':self.public_key}
        else:
            headers = None

        logging.debug('[REST_MASTER] QUERY URL {0}'.format(urlQuery))
       	api_resp = requests.request(method, urlQuery, headers=headers)
        data = api_resp.json()
        logging.debug('[REST_MASTER] QUERY DATA {0}'.format(data))

        if 'code' in data:
            logging.warning('[BINANCE_API_ERROR][CODE: "{0}"][MESSAGE: "{1}"]'.format(data['code'], data['msg']))

        self.requests_made += 1

        return(data)