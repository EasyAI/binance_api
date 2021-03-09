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
        self.session = requests.Session()
        self.requests_made  = 0
        self.errors         = 0

        self.default_api_type   = default_api_type
        self.public_key         = public_key
        self.private_key        = private_key


    ## ------------------ [BLVT_EXCLUSIVE] ------------------ ##
    def get_blvt_info(self, **kwargs):
        return(self.param_check(blvt_api.get_blvt_info, kwargs))
    def subscribe_blvt(self, **kwargs):
        return(self.param_check(blvt_api.subscribe_blvt, kwargs))
    def query_subscription_record(self, **kwargs):
        return(self.param_check(blvt_api.query_subscription_record, kwargs))
    def redeem_blvt(self, **kwargs):
        return(self.param_check(blvt_api.redeem_blvt, kwargs))
    def query_redemption_record(self, **kwargs):
        return(self.param_check(blvt_api.query_redemption_record, kwargs))
    def get_blvt_userLimit(self, **kwargs):
        return(self.param_check(blvt_api.get_blvt_userLimit, kwargs))

    ## ------------------ [BSWAP_EXCLUSIVE] ------------------ ##
    def get_swap_pools(self):
        return(self.param_check(bswap_api.get_swap_pools))
    def get_liquidity_poolInfo(self, **kwargs):
        return(self.param_check(bswap_api.get_liquidity_poolInfo, kwargs))
    def add_liquidity(self, **kwargs):
        return(self.param_check(bswap_api.add_liquidity, kwargs))
    def remove_liquidity(self, **kwargs):
        return(self.param_check(bswap_api.remove_liquidity, kwargs))
    def get_liquidity_record(self, **kwargs):
        return(self.param_check(bswap_api.get_liquidity_record, kwargs))
    def get_quote(self, **kwargs):
        return(self.param_check(bswap_api.get_quote, kwargs))
    def make_swap(self, **kwargs):
        return(self.param_check(bswap_api.make_swap, kwargs))
    def get_swap_history(self, **kwargs):
        return(self.param_check(bswap_api.get_swap_history, kwargs))

    ## ------------------ [FUTURES_EXCLUSIVE] ------------------ ##
    def futures_transfer(self, **kwargs):
        return(self.param_check(futures_api.futures_transfer, kwargs))
    def get_futures_transactions(self, **kwargs):
        return(self.param_check(futures_api.get_futures_transactions, kwargs))
    def borrow_crossCollat(self, **kwargs):
        return(self.param_check(futures_api.borrow_crossCollat, kwargs))
    def get_crossCollat_borrowHist(self, **kwargs):
        return(self.param_check(futures_api.get_crossCollat_borrowHist, kwargs))
    def repay_crossCollat(self, **kwargs):
        return(self.param_check(futures_api.repay_crossCollat, kwargs))
    def get_crossCollat_repayHist(self, **kwargs):
        return(self.param_check(futures_api.get_crossCollat_repayHist, kwargs))
    def get_crossCollat_wallet(self):
        return(self.param_check(futures_api.get_crossCollat_wallet))
    def get_crossCollat_wallet_v2(self):
        return(self.param_check(futures_api.get_crossCollat_wallet_v2))
    def get_crossCollat_info(self, **kwargs):
        return(self.param_check(futures_api.get_crossCollat_info, kwargs))
    def get_crossCollat_info_v2(self, **kwargs):
        return(self.param_check(futures_api.get_crossCollat_info_v2, kwargs))
    def get_crossCollat_rate_LTV(self, **kwargs):
        return(self.param_check(futures_api.get_crossCollat_rate_LTV, kwargs))
    def get_crossCollat_rate_LTV_v2(self, **kwargs):
        return(self.param_check(futures_api.get_crossCollat_rate_LTV_v2, kwargs))
    def get_crossCollat_max_LTV(self, **kwargs):
        return(self.param_check(futures_api.get_crossCollat_max_LTV, kwargs))
    def get_crossCollat_max_LTV_v2(self, **kwargs):
        return(self.param_check(futures_api.get_crossCollat_max_LTV_v2, kwargs))
    def adjust_crossCollat_LTV(self, **kwargs):
        return(self.param_check(futures_api.adjust_crossCollat_LTV, kwargs))
    def adjust_crossCollat_LTV_v2(self, **kwargs):
        return(self.param_check(futures_api.adjust_crossCollat_LTV_v2, kwargs))
    def adjust_crossCollat_LTV_history(self, **kwargs):
        return(self.param_check(futures_api.adjust_crossCollat_LTV_history, kwargs))
    def adjust_crossCollat_liquidation_history(self, **kwargs):
        return(self.param_check(futures_api.adjust_crossCollat_liquidation_history, kwargs))
    def get_collatRepay_limit(self, **kwargs):
        return(self.param_check(futures_api.get_collatRepay_limit, kwargs))
    def get_collatRepay_quote(self, **kwargs):
        return(self.param_check(futures_api.get_collatRepay_quote, kwargs))
    def collateral_repay(self, **kwargs):
        return(self.param_check(futures_api.collateral_repay, kwargs))
    def get_collatRepay_result(self, **kwargs):
        return(self.param_check(futures_api.get_collatRepay_result, kwargs))
    def get_crossCollat_interestHist(self, **kwargs):
        return(self.param_check(futures_api.get_crossCollat_interestHist, kwargs))

    ## ------------------ [MARGIN_EXCLUSIVE] ------------------ ##
    def margin_transfer(self, **kwargs):
        return(self.param_check(margin_api.margin_transfer, kwargs))
    def margin_accountBorrow(self, **kwargs):
        return(self.param_check(margin_api.margin_accountBorrow, kwargs))
    def margin_accountRepay(self, **kwargs):
        return(self.param_check(margin_api.margin_accountRepay, kwargs))
    def query_margin_asset(self, **kwargs):
        return(self.param_check(margin_api.query_margin_asset, kwargs))
    def query_crossPair(self, **kwargs):
        return(self.param_check(margin_api.query_crossPair, kwargs))
    def get_margin_allAssets(self):
        return(self.param_check(margin_api.get_margin_allAssets))
    def get_allCrossPairs(self):
        return(self.param_check(margin_api.get_allCrossPairs))
    def query_margin_priceIndex(self, **kwargs):
        return(self.param_check(margin_api.query_margin_priceIndex, kwargs))
    def get_margin_crossTransferHistory(self, **kwargs):
        return(self.param_check(margin_api.get_margin_crossTransferHistory, kwargs))
    def get_loanRecord(self, **kwargs):
        return(self.param_check(margin_api.get_loanRecord, kwargs))
    def get_repayRecord(self, **kwargs):
        return(self.param_check(margin_api.get_repayRecord, kwargs))
    def get_interestHistory(self, **kwargs):
        return(self.param_check(margin_api.get_interestHistory, kwargs))
    def get_fLiquidationRecord(self, **kwargs):
        return(self.param_check(margin_api.get_fLiquidationRecord, kwargs))
    def get_cross_accountDetails(self):
        return(self.param_check(margin_api.get_cross_accountDetails))
    def get_maxBorrow(self, **kwargs):
        return(self.param_check(margin_api.get_maxBorrow, kwargs))
    def get_maxOutAmmount(self, **kwargs):
        return(self.param_check(margin_api.get_maxOutAmmount, kwargs))
    def create_isolatedMaringAccount(self, **kwargs):
        return(self.param_check(margin_api.create_isolatedMaringAccount, kwargs))
    def isolated_transfer(self, **kwargs):
        return(self.param_check(margin_api.isolated_transfer, kwargs))
    def get_isolated_transferHistory(self, **kwargs):
        return(self.param_check(margin_api.get_isolated_transferHistory, kwargs))
    def get_isolated_accountInfo(self, **kwargs):
        return(self.param_check(margin_api.get_isolated_accountInfo, kwargs))
    def get_isolated_symbol(self, **kwargs):
        return(self.param_check(margin_api.get_isolated_symbol, kwargs))
    def get_isolated_symbol_all(self):
        return(self.param_check(margin_api.get_isolated_symbol_all))
    def toggle_BNB_burn_ST_MI(self, **kwargs):
        return(self.param_check(margin_api.toggle_BNB_burn_ST_MI, kwargs))
    def get_BNB_burn_status(self):
        return(self.param_check(margin_api.get_BNB_burn_status))

    ## ------------------ [MARKET_DATA_EXCLUSIVE] ------------------ ##
    def test_ping(self):
        return(self.param_check(marketData_api.test_ping))
    def get_serverTime(self):
        return(self.param_check(marketData_api.get_serverTime))
    def get_exchangeInfo(self):
        return(self.param_check(marketData_api.get_exchangeInfo))
    def get_orderBook(self, **kwargs):
        return(self.param_check(marketData_api.get_orderBook, kwargs))
    def get_custom_trades(self, **kwargs):
        if kwargs['limit'] > 1000:
            kwargs.update({'pubKey':self.public_key, 'prvKey':self.private_key})
        return(custom_data_formatter.get_custom_trades(kwargs))
    def get_recentTrades(self, **kwargs):
        return(custom_data_formatter.get_custom_trades(self.param_check(marketData_api.get_recentTrades, kwargs)))
    def get_oldTrades(self, **kwargs):
        return(custom_data_formatter.get_custom_trades(self.param_check(marketData_api.get_oldTrades, kwargs)))
    def get_aggTradeList(self, **kwargs):
        return(self.param_check(marketData_api.get_aggTradeList, kwargs))
    def get_custom_candles(self, **kwargs):
        return(custom_data_formatter.get_custom_candles(kwargs))
    def get_candles(self, **kwargs):
        return(formatter.format_candles(self.param_check(marketData_api.get_candles, kwargs), 'REST'))
    def get_averagePrice(self, **kwargs):
        return(self.param_check(marketData_api.get_averagePrice, kwargs))
    def get_24hTicker(self, **kwargs):
        return(self.param_check(marketData_api.get_24hTicker, kwargs))
    def get_priceTicker(self, **kwargs):
        return(self.param_check(marketData_api.get_priceTicker, kwargs))
    def get_orderbookTicker(self, **kwargs):
        return(self.param_check(marketData_api.get_orderbookTicker, kwargs))

    ## ------------------ [MINING_EXCLUSIVE] ------------------ ##
    def get_algorithm(self):
        return(self.param_check(mining_api.get_algorithm))
    def get_coinNames(self):
        return(self.param_check(mining_api.get_coinNames))
    def get_minerList_detail(self, **kwargs):
        return(self.param_check(mining_api.get_minerList_detail, kwargs))
    def get_minerList(self, **kwargs):
        return(self.param_check(mining_api.get_minerList, kwargs))
    def get_earningsList(self, **kwargs):
        return(self.param_check(mining_api.get_earningsList, kwargs))
    def get_extraBonusList(self, **kwargs):
        return(self.param_check(mining_api.get_extraBonusList, kwargs))
    def get_hashrateResaleList(self, **kwargs):
        return(self.param_check(mining_api.get_hashrateResaleList, kwargs))
    def get_hashrateResaleDetail(self, **kwargs):
        return(self.param_check(mining_api.get_hashrateResaleDetail, kwargs))
    def post_hashrateResale(self, **kwargs):
        return(self.param_check(mining_api.post_hashrateResale, kwargs))
    def cancel_hashrateResale(self, **kwargs):
        return(self.param_check(mining_api.cancel_hashrateResale, kwargs))
    def get_statisticList(self, **kwargs):
        return(self.param_check(mining_api.get_statisticList, kwargs))
    def get_accountList(self, **kwargs):
        return(self.param_check(mining_api.get_accountList, kwargs))

    ## ------------------ [SAVINGS_EXCLUSIVE] ------------------ ##
    def get_productList(self, **kwargs):
        return(self.param_check(savings_api.get_productList, kwargs))
    def get_dailyPurchaseQuota(self, **kwargs):
        return(self.param_check(savings_api.get_dailyPurchaseQuota, kwargs))
    def purchase_product(self, **kwargs):
        return(self.param_check(savings_api.purchase_product, kwargs))
    def get_dailyRedemptionQuota(self, **kwargs):
        return(self.param_check(savings_api.get_dailyRedemptionQuota, kwargs))
    def redeem_product(self, **kwargs):
        return(self.param_check(savings_api.redeem_product, kwargs))
    def get_product_position(self, **kwargs):
        return(self.param_check(savings_api.get_product_position, kwargs))
    def get_FnAProject_list(self, **kwargs):
        return(self.param_check(savings_api.get_FnAProject_list, kwargs))
    def purchase_FnAProject(self, **kwargs):
        return(self.param_check(savings_api.purchase_FnAProject, kwargs))
    def get_FnAProject_position(self, **kwargs):
        return(self.param_check(savings_api.get_FnAProject_position, kwargs))
    def get_lending(self):
        return(self.param_check(savings_api.get_lending))
    def get_purchase_record(self, **kwargs):
        return(self.param_check(savings_api.get_purchase_record, kwargs))
    def get_redemption_record(self, **kwargs):
        return(self.param_check(savings_api.get_redemption_record, kwargs))
    def get_interest_history(self, **kwargs):
        return(self.param_check(savings_api.get_interest_history, kwargs))
    def change_position(self, **kwargs):
        return(self.param_check(savings_api.change_position, kwargs))

    ## ------------------ [SPOT_EXCLUSIVE] ------------------ ##
    def place_order_test(self, **kwargs):
        return(self.param_check(spot_api.place_order_test, kwargs))
    def place_order_oco(self, **kwargs):
        return(self.param_check(spot_api.place_order_oco, kwargs))
    def cancel_order_oco(self, **kwargs):
        return(self.param_check(spot_api.cancel_order_oco, kwargs))
    def query_order_oco(self, **kwargs):
        return(self.param_check(spot_api.query_order_oco, kwargs))
    def get_all_orders_oco(self, **kwargs):
        return(self.param_check(spot_api.get_all_orders_oco, kwargs))
    def get_open_orders_oco(self):
        return(self.param_check(spot_api.get_open_orders_oco))
    def get_accountInfo(self):
        return(self.param_check(spot_api.get_accountInfo))

    ## ------------------ [SUB-ACCOUNT_EXCLUSIVE] ------------------ ##
    def get_subAccount_list(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_list, kwargs))
    def get_subAccount_spotTransferHistory_wapi(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_spotTransferHistory_wapi, kwargs))
    def get_subAccount_spotTransferHistory_sapi(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_spotTransferHistory_sapi, kwargs))
    def subAccount_spotAsset_transfer(self, **kwargs):
        return(self.param_check(subAccount_api.subAccount_spotAsset_transfer, kwargs))
    def get_subAccount_futuresTransferHistory(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_futuresTransferHistory, kwargs))
    def subAccount_futuresAsset_transfer(self, **kwargs):
        return(self.param_check(subAccount_api.subAccount_futuresAsset_transfer, kwargs))
    def get_subAccount_assets(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_assets, kwargs))
    def get_subAccount_spotAssetsSummary(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_spotAssetsSummary, kwargs))
    def get_subAccount_depositAddress(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_depositAddress, kwargs))
    def get_subAccount_depositHistory(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_depositHistory, kwargs))
    def get_subAccount_statusFnM(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_statusFnM, kwargs))
    def enable_subAccount_margin(self, **kwargs):
        return(self.param_check(subAccount_api.enable_subAccount_margin, kwargs))
    def get_subAccount_marginAccount(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_marginAccount, kwargs))
    def get_subAccount_marginAccountSummary(self):
        return(self.param_check(subAccount_api.get_subAccount_marginAccountSummary))
    def enable_subAccount_futures(self, **kwargs):
        return(self.param_check(subAccount_api.enable_subAccount_futures, kwargs))
    def get_subAccount_futuresAccount(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_futuresAccount, kwargs))
    def get_subAccount_futuresAccountSummary(self):
        return(self.param_check(subAccount_api.get_subAccount_futuresAccountSummary))
    def get_subAccount_positionRisk(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_positionRisk, kwargs))
    def subAccount_futures_transfer(self, **kwargs):
        return(self.param_check(subAccount_api.subAccount_futures_transfer, kwargs))
    def subAccount_margin_transfer(self, **kwargs):
        return(self.param_check(subAccount_api.subAccount_margin_transfer, kwargs))
    def master_sub_transfer(self, **kwargs):
        return(self.param_check(subAccount_api.master_sub_transfer, kwargs))
    def sub_master_transfer(self, **kwargs):
        return(self.param_check(subAccount_api.sub_master_transfer, kwargs))
    def get_subAccount_transferHistory(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_transferHistory, kwargs))
    def make_universalTransfer(self, **kwargs):
        return(self.param_check(subAccount_api.make_universalTransfer, kwargs))
    def get_universalTransferHisotry(self, **kwargs):
        return(self.param_check(subAccount_api.get_universalTransferHisotry, kwargs))
    def get_subAccount_futuresAccount_v2(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_futuresAccount_v2, kwargs))
    def get_subAccount_futuresAccountSummary_v2(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_futuresAccountSummary_v2, kwargs))
    def get_subAccount_positionRisk_v2(self, **kwargs):
        return(self.param_check(subAccount_api.get_subAccount_positionRisk_v2, kwargs))

    ## ------------------ [WALLET_EXCLUSIVE] ------------------ ##
    def get_systemStatus(self):
        return(self.param_check(wallet_api.get_systemStatus))
    def get_allCoinsInfo(self):
        return(self.param_check(wallet_api.get_allCoinsInfo))
    def get_dailySnapshot(self, **kwargs):
        return(self.param_check(wallet_api.get_dailySnapshot, kwargs))
    def disable_withdrawSwitch(self):
        return(self.param_check(wallet_api.disable_withdrawSwitch))
    def enable_withdrawSwitch(self):
        return(self.param_check(wallet_api.enable_withdrawSwitch))
    def make_withdraw_SAPI(self, **kwargs):
        return(self.param_check(wallet_api.make_withdraw_SAPI, kwargs))
    def make_withdraw(self, **kwargs):
        return(self.param_check(wallet_api.make_withdraw, kwargs))
    def get_depositHistory_SN(self, **kwargs):
        return(self.param_check(wallet_api.get_depositHistory_SN, kwargs))
    def get_depositHistory(self, **kwargs):
        return(self.param_check(wallet_api.get_depositHistory, kwargs))
    def get_withdrawHistory_SN(self, **kwargs):
        return(self.param_check(wallet_api.get_withdrawHistory_SN, kwargs))
    def get_withdrawHistory(self, **kwargs):
        return(self.param_check(wallet_api.get_withdrawHistory, kwargs))
    def depositAddress_SN(self, **kwargs):
        return(self.param_check(wallet_api.depositAddress_SN, kwargs))
    def depositAddress(self, **kwargs):
        return(self.param_check(wallet_api.depositAddress, kwargs))
    def get_accountStatus(self):
        return(self.param_check(wallet_api.get_accountStatus))
    def get_apiStatus(self):
        return(self.param_check(wallet_api.get_apiStatus))
    def get_dustLog(self):
        return(self.param_check(wallet_api.get_dustLog))
    def make_dustTransfer(self, **kwargs):
        return(self.param_check(wallet_api.make_dustTransfer, kwargs))
    def get_dividendRecord(self, **kwargs):
        return(self.param_check(wallet_api.get_dividendRecord, kwargs))
    def get_assetDetail(self):
        return(self.param_check(wallet_api.get_assetDetail))
    def get_tradeFee(self, **kwargs):
        return(self.param_check(wallet_api.get_tradeFee, kwargs))
    def make_universalTransfer(self, **kwargs):
        return(self.param_check(wallet_api.make_universalTransfer, kwargs))
    def get_universalTransferHistory(self, **kwargs):
        return(self.param_check(wallet_api.get_universalTransferHistory, kwargs))

    ## ------------------ [USER_DATA_STREAM_EXCLUSIVE] ------------------ ##
    def get_listenKey(self, api_type=None):
        if api_type == 'SPOT':      return(self.param_check(userDataStream_api.get_listenKey_spot))
        elif api_type == 'MARGIN':  return(self.param_check(userDataStream_api.get_listenKey_margin))
        elif api_type == 'FUTURES': return(self.param_check(userDataStream_api.send_listenKey_keepAlive_margin, kwargs))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT/FUTURES)')

    def send_listenKey_keepAlive(self, api_type='SPOT', **kwargs):
        if api_type == 'SPOT':      return(self.param_check(userDataStream_api.send_listenKey_keepAlive_spot, kwargs))
        elif api_type == 'MARGIN':  return(self.param_check(userDataStream_api.send_listenKey_keepAlive_margin, kwargs))
        elif api_type == 'FUTURES': return(self.param_check(userDataStream_api.send_listenKey_keepAlive_margin, kwargs))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT/FUTURES)')

    def close_listenKey(self, api_type='SPOT', **kwargs):
        if api_type == 'SPOT':      return(self.param_check(userDataStream_api.close_listenKey_spot, kwargs))
        elif api_type == 'MARGIN':  return(self.param_check(userDataStream_api.close_listenKey_margin, kwargs))
        elif api_type == 'FUTURES': return(self.param_check(userDataStream_api.send_listenKey_keepAlive_margin, kwargs))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT/FUTURES)')


    ## ------------------ [MULTI_API_ENDPOINT] ------------------ ##
    def get_account(self, api_type=None):
        if api_type == None: api_type = self.default_api_type
        if api_type == 'SPOT':      return(self.param_check(spot_api.get_accountInfo))
        elif api_type == 'MARGIN':  return(self.param_check(margin_api.get_cross_accountDetails))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def place_order(self, api_type=None, **kwargs):
        if api_type == None: api_type = self.default_api_type
        if api_type == 'SPOT':      return(self.param_check(spot_api.place_order, kwargs))
        elif api_type == 'MARGIN':  return(self.param_check(margin_api.place_order, kwargs))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def get_order(self, api_type=None, **kwargs):
        if api_type == None: api_type = self.default_api_type
        if api_type == 'SPOT':      return(self.param_check(spot_api.get_order, kwargs))
        elif api_type == 'MARGIN':  return(self.param_check(margin_api.get_order, kwargs))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def cancel_order(self, api_type=None, **kwargs):
        if api_type == None: api_type = self.default_api_type
        if api_type == 'SPOT':      return(self.param_check(spot_api.cancel_order, kwargs))
        elif api_type == 'MARGIN':  return(self.param_check(margin_api.cancel_order, kwargs))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def cancel_all_orders(self, api_type=None, **kwargs):
        if api_type == None: api_type = self.default_api_type
        if api_type == 'SPOT':      return(self.param_check(spot_api.cancel_all_orders, kwargs))
        elif api_type == 'MARGIN':  return(self.param_check(margin_api.cancel_all_orders, kwargs))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def get_all_orders(self, api_type=None, **kwargs):
        if api_type == None: api_type = self.default_api_type
        if api_type == 'SPOT':      return(self.param_check(spot_api.get_all_orders, kwargs))
        elif api_type == 'MARGIN':  return(self.param_check(margin_api.get_all_orders, kwargs))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def get_all_trades(self, api_type=None, **kwargs):
        if api_type == None: api_type = self.default_api_type
        if api_type == 'SPOT':      return(self.param_check(spot_api.get_all_trades, kwargs))
        elif api_type == 'MARGIN':  return(self.param_check(margin_api.get_all_trades, kwargs))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def get_open_orders(self, api_type=None, **kwargs):
        if api_type == None: api_type = self.default_api_type
        if api_type == 'SPOT':      return(self.param_check(spot_api.get_open_orders, kwargs))
        elif api_type == 'MARGIN':  return(self.param_check(margin_api.get_open_orders, kwargs))
        elif api_type == None:      return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')


    def param_check(self, api_info, users_passed_parameters=None):
        if users_passed_parameters==None or not('IS_TEST' in users_passed_parameters):
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
        else: 
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
       	api_resp = self.session.request(method, urlQuery, headers=headers)
        data = api_resp.json()
        logging.debug('[REST_MASTER] QUERY DATA {0}'.format(data))

        if 'code' in data:
            logging.warning('[BINANCE_API_ERROR][CODE: "{0}"][MESSAGE: "{1}"]'.format(data['code'], data['msg']))

        self.requests_made += 1

        return(data)