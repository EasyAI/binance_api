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
from . import spot_api
from . import wapi_api
from . import margin_api
from . import userDataStream_api


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


    ## ------------------ [SPOT_EXCLUSIVE] ------------------ ##
    def test_ping(self):
        return(self.param_check(spot_api.test_ping))

    def check_time(self):
        return(self.param_check(spot_api.check_time))

    def get_exchange_info(self):
        return(self.param_check(spot_api.get_exchange_info))

    def get_market_depth(self, **kwargs):
        return(self.param_check(spot_api.get_market_depth, kwargs))

    def get_custom_trades(self, **kwargs):
        if kwargs['limit'] > 1000:
            kwargs.update({'pubKey':self.public_key, 'prvKey':self.private_key})
        return(custom_data_formatter.get_custom_trades(kwargs))

    def get_recent_trades(self, **kwargs):
        trades_data = self.param_check(spot_api.get_recent_trades, kwargs)
        return(formatter.format_trades(trades_data))

    def get_historical_trades(self, **kwargs):
        trades_data = self.param_check(spot_api.get_historical_trades, kwargs)
        return(formatter.format_trades(trades_data))

    def get_agg_trades(self, **kwargs):
        return(self.param_check(spot_api.get_agg_trades, kwargs))

    def get_custom_candles(self, **kwargs):
        return(custom_data_formatter.get_custom_candles(kwargs))

    def get_candles(self, **kwargs):
        candle_data = self.param_check(spot_api.get_candles, kwargs)
        if not('error' in candle_data or 'code' in candle_data):
            return(formatter.format_candles(candle_data, 'SPOT'))
        else: return(candle_data)

    def get_avg_price(self, **kwargs):
        return(self.param_check(spot_api.get_avg_price, kwargs))

    def get_market_24h(self, **kwargs):
        return(self.param_check(spot_api.get_market_24h, kwargs))

    def get_latest_price(self, **kwargs):
        return(self.param_check(spot_api.get_latest_price, kwargs))

    def get_book_ticker(self, **kwargs):
        return(self.param_check(spot_api.get_book_ticker, kwargs))

    def get_order(self, **kwargs):
        return(self.param_check(spot_api.get_order, kwargs))

    def cancel_open_orders(self, **kwargs):
        return(self.param_check(spot_api.cancel_open_orders, kwargs))

    def place_oco_order(self, **kwargs):
        return(self.param_check(spot_api.place_oco_order, kwargs))

    def cancel_oco_order(self, **kwargs):
        return(self.param_check(spot_api.cancel_oco_order, kwargs))

    def get_oco_order(self, **kwargs):
        return(self.param_check(spot_api.get_oco_order, kwargs))

    def get_all_oco_orders(self, **kwargs):
        return(self.param_check(spot_api.get_all_oco_orders, kwargs))

    def get_open_oco_orders(self):
        return(self.param_check(spot_api.get_open_oco_orders))


    ## ------------------ [WAPI_EXCLUSIVE] ------------------ ##
    def make_withdraw(self, **kwargs):
        return(self.param_check(wapi_api.make_withdraw, kwargs))

    def get_deposit_history(self, **kwargs):
        return(self.param_check(wapi_api.get_deposit_history, kwargs))

    def get_withdraw_history(self, **kwargs):
        return(self.param_check(wapi_api.get_withdraw_history, kwargs))

    def get_deposit_Address(self, **kwargs):
        return(self.param_check(wapi_api.get_deposit_Address, kwargs))

    def get_account_status(self):
        return(self.param_check(wapi_api.get_account_status))

    def get_system_status(self):
        return(self.param_check(wapi_api.get_system_status))

    def get_account_api_trading_status(self):
        return(self.param_check(wapi_api.get_account_api_trading_status))

    def get_dustLog(self):
        return(self.param_check(wapi_api.get_dustLog))

    def get_tradeFee(self, **kwargs):
        return(self.param_check(wapi_api.get_tradeFee, kwargs))

    def get_assetDetails(self):
        return(self.param_check(wapi_api.get_assetDetails))

    def get_subAccounts(self, **kwargs):
        return(self.param_check(wapi_api.get_subAccounts, kwargs))

    def get_subAccounts_transfers(self, **kwargs):
        return(self.param_check(wapi_api.get_subAccounts_transfers, kwargs))

    def make_subAccounts_transfer(self, **kwargs):
        return(self.param_check(wapi_api.make_subAccounts_transfer, kwargs))

    def get_subAccounts_assets(self, **kwargs):
        return(self.param_check(wapi_api.get_subAccounts_assets, kwargs))

    def dust_transfer(self, **kwargs):
        return(self.param_check(wapi_api.dust_transfer, kwargs))

    def get_assetDividendRecord(self, **kwargs):
        return(self.param_check(wapi_api.get_assetDividendRecord, kwargs))


    ## ------------------ [MARGIN_EXCLUSIVE] ------------------ ##
    def transfer_to_margin(self, **kwargs):
        return(self.param_check(margin_api.transfer_to_margin, kwargs))

    def apply_for_loan(self, **kwargs):
        return(self.param_check(margin_api.apply_for_loan, kwargs))

    def repay_loan(self, **kwargs):
        return(self.param_check(margin_api.repay_loan, kwargs))

    def get_loan_record(self, **kwargs):
        return(self.param_check(margin_api.get_loan_record, kwargs))

    def get_repayed_record(self, **kwargs):
        return(self.param_check(margin_api.get_repayed_record, kwargs))

    def get_asset(self, **kwargs):
        return(self.param_check(margin_api.get_asset, kwargs))

    def get_market_info(self, **kwargs):
        return(self.param_check(margin_api.get_market_info, kwargs))

    def get_all_assets(self):
        return(self.param_check(margin_api.get_all_assets))

    def get_all_markets(self):
        return(self.param_check(margin_api.get_all_markets))

    def get_margin_priceIndex(self, **kwargs):
        return(self.param_check(margin_api.get_margin_priceIndex, kwargs))

    def get_transfer_history(self, **kwargs):
        return(self.param_check(margin_api.get_transfer_history, kwargs))

    def get_interest_history(self, **kwargs):
        return(self.param_check(margin_api.get_interest_history, kwargs))

    def get_liquidation_record(self, **kwargs):
        return(self.param_check(margin_api.get_liquidation_record, kwargs))

    def get_market_orders(self, **kwargs):
        return(self.param_check(margin_api.get_market_orders, kwargs))

    def get_max_borrow_amount(self, **kwargs):
        return(self.param_check(margin_api.get_max_borrow_amount, kwargs))

    def get_max_transfer_amount(self, **kwargs):
        return(self.param_check(margin_api.get_max_transfer_amount, kwargs))


    ## ------------------ [USER_DATA_STREAM_EXCLUSIVE] ------------------ ##
    def get_listenKey(self, api_type=None):
        if api_type == 'SPOT':
            return(self.param_check(userDataStream_api.get_listenKey_spot))
        elif api_type == 'MARGIN':
            return(self.param_check(userDataStream_api.get_listenKey_margin))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def send_listenKey_keepAlive(self, api_type='SPOT', **kwargs):
        if api_type == 'SPOT':
            return(self.param_check(userDataStream_api.send_listenKey_keepAlive_spot, kwargs))
        elif api_type == 'MARGIN':
            return(self.param_check(userDataStream_api.send_listenKey_keepAlive_margin, kwargs))
        elif api_type == None:
            return('PLEASE_SPECIFY_API_TYPE, api_type=(MARGIN/SPOT)')

    def close_listenKey(self, api_type='SPOT', **kwargs):
        if api_type == 'SPOT':
            return(self.param_check(userDataStream_api.close_listenKey_spot, kwargs))
        elif api_type == 'MARGIN':
            return(self.param_check(userDataStream_api.close_listenKey_margin, kwargs))
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