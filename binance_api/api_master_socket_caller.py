#! /usr/bin/env python3

import sys
import copy
import time
import json
import hashlib
import logging
import websocket
import threading

from . import api_support_tools
from . import formatter
from . import websocket_api

## sets up the socket BASE for binances socket API.
SOCKET_BASE = 'wss://stream.binance.com:9443'


class Binance_SOCK:

    def __init__(self):
        '''
        Setup the connection and setup data containers and management variables for the socket.
        '''
        self.MAX_REQUEST_ITEMS      = 10
        self.requested_items        = {}

        self.last_data_recv_time    = 0

        self.socketRunning          = False
        self.socketBuffer           = {}
        self.ws                     = None
        self.stream_names           = []
        self.query                  = ''
        self.id_counter             = 0

        self.BASE_CANDLE_LIMIT      = 200
        self.BASE_DEPTH_LIMIT       = 20

        ## For locally managed data.
        self.live_and_historic_data = False
        self.candle_data            = {}
        self.book_data              = {}
        self.reading_books          = False

        self.userDataStream_added   = False
        self.listen_key             = None


    def build_query(self):
        self.query = ''

        if len(self.stream_names) == 0 or self.stream_names == []:
            return('NO_STREAMS_SET')

        elif len(self.stream_names) == 1:
            query = '{0}/ws/{1}'.format(SOCKET_BASE, self.stream_names[0])

        else:
            query = '{0}/stream?streams='.format(SOCKET_BASE)

            for i, stream_name in enumerate(self.stream_names):
                query += stream_name
                if i != len(self.stream_names) - 1:
                    query+='/'

        self.query = query
        return('QUERY_BUILT_SUCCESSFULLY')


    def clear_query(self):
        self.query              = ''
        self.stream_names       = []
        self.candles_markets    = []
        self.book_markets       = []

        return('QUERY_CLEARED')


    ## ------------------ [DATA_ACCESS_ENDPOINT] ------------------ ##
    def get_live_depths(self, symbol=None):
        got_books = False
        return_books = {}

        while not(got_books):
            got_books = True
            for key in self.book_data:
                try:
                    ask_Price_List = self._orderbook_sorter_algo(copy.deepcopy(self.book_data[key]['a']), 'ask')
                    bid_Price_List = self._orderbook_sorter_algo(copy.deepcopy(self.book_data[key]['b']), 'bid')
                    return_books.update({key:{'a':ask_Price_List, 'b':bid_Price_List}})
                except RuntimeError as error:
                    if error == 'dictionary changed size during iteration':
                        print('dodged book error')
                    got_books = False
                    break

        if symbol:
            if not symbol in return_books:
                print(return_books)
            return(return_books[symbol])

        return(return_books)

    def get_live_candles(self, symbol=None):
        if symbol:
            return(self.candle_data[symbol])
        return(self.candle_data)


    ## ------------------ [MANUAL_CALLS_EXCLUSIVE] ------------------ ##
    def subscribe_streams(self, **kwargs):
        return(self._send_message('SUBSCRIBE', **kwargs))

    def unsubscribe_streams(self, **kwargs):
        return(self._send_message('UNSUBSCRIBE', **kwargs))

    def get_current_streams(self):
        return(self._send_message('LIST_SUBSCRIPTIONS'))

    def set_property(self, **kwargs):
        ''' combined = true'''
        return(self._send_message('SET_PROPERTY', **kwargs))

    def get_property(self):
        return(self._send_message('GET_PROPERTY'))


    ## ------------------ [WEBSOCKET_EXCLUSIVE] ------------------ ##
    def set_aggTrade_stream(self, **kwargs):
        return(self.make_api_call(websocket_api.set_aggTrade_stream, kwargs))

    def set_trade_stream(self, **kwargs):
        return(self.make_api_call(websocket_api.set_trade_stream, kwargs))

    def set_candle_stream(self, **kwargs):
        return(self.make_api_call(websocket_api.set_candle_stream, kwargs))

    def set_miniTicker_stream(self, **kwargs):
        return(self.make_api_call(websocket_api.set_miniTicker_stream, kwargs))

    def set_global_miniTicker_stream(self):
        return(self.make_api_call(websocket_api.set_global_miniTicker_stream))

    def set_ticker_stream(self, **kwargs):
        return(self.make_api_call(websocket_api.set_ticker_stream, kwargs))

    def set_gloal_ticker_stream(self):
        return(self.make_api_call(websocket_api.set_gloal_ticker_stream))

    def set_bookTicker_stream(self, **kwargs):
        return(self.make_api_call(websocket_api.set_bookTicker_stream, kwargs))

    def set_global_bookTicker_stream(self):
        return(self.make_api_call(websocket_api.set_global_bookTicker_stream))

    def set_partialBookDepth_stream(self, **kwargs):
        return(self.make_api_call(websocket_api.set_partialBookDepth_stream, kwargs))

    def set_manual_depth_stream(self, **kwargs):
        return(self.make_api_call(websocket_api.set_manual_depth_stream, kwargs))


    ## ------------------ [FULL_DATA_EXCLUSIVE] ------------------ ##
    def set_live_and_historic_combo(self, rest_api):
        if not(self.live_and_historic_data):
            for stream in self.stream_names:
                symbol = stream.split('@')[0].upper()
                if 'kline' in stream:
                    self._set_initial_candles(symbol, stream.split('_')[1], rest_api)
                if 'depth' in stream:
                    self._set_initial_depth(symbol, rest_api)
                time.sleep(1)

            RETURN_MESSAGE = 'STARTED_HISTORIC_DATA'
        else:
            if self.candle_data != {}:
                self.candle_data = {}

            RETURN_MESSAGE = 'STOPPED_HISTORIC_DATA'

        self.live_and_historic_data = not(self.live_and_historic_data)

        return(RETURN_MESSAGE)


    ## ------------------ [USER_DATA_STREAM_EXCLUSIVE] ------------------ ##
    def set_userDataStream(self, AUTHENTICATED_REST, user_data_stream_type, remove_stream=False):
        if remove_stream:
            message = self.make_api_call(None, {'listenKey':self.listen_key, 'remove_stream':True})
            self.listen_key = None
        else:
            if self.listen_key == None:

                key_auth = AUTHENTICATED_REST.get_listenKey(user_data_stream_type)
                listen_key = key_auth['listenKey']

                message = self.make_api_call(None, {'listenKey':listen_key})
                self.listen_key = listen_key

                logging.info('[SOCKET_MASTER] Starting local managing')
                lkkaT = threading.Thread(target=self.listenKey_keepAlive, args=(AUTHENTICATED_REST,user_data_stream_type))
                lkkaT.start()

        return(message)


    def listenKey_keepAlive(self, AUTHENTICATED_REST, user_data_stream_type):
        lastUpdate = time.time()

        while self.listen_key != None:
            if (lastUpdate + 1800) < time.time():
                AUTHENTICATED_REST.send_listenKey_keepAlive(user_data_stream_type, listenKey=self.listen_key)
                lastUpdate = time.time()

            time.sleep(1)


    def make_api_call(self, api_info, users_passed_parameters={}):
        if 'listenKey' not in users_passed_parameters:
            if 'symbol' in users_passed_parameters:
                if '-' in users_passed_parameters['symbol']:
                    base, quote = users_passed_parameters['symbol'].split('-')
                    users_passed_parameters.update({'symbol':(quote+base).lower()})
                    
            target_endpoint, params, headers, body = api_support_tools.param_check(api_info, users_passed_parameters)
            stream_name = target_endpoint
        else:
            stream_name = users_passed_parameters['listenKey']

        if 'remove_stream' in users_passed_parameters:
            if users_passed_parameters['remove_stream']:
                if stream_name in self.stream_names:
                    self.stream_names.remove(stream_name)
                return({'result':'REMOVED_STREAM_NAME', 'stream':stream_name})

                if self.ws != None and self.socketRunning:
                    self.unsubscribe_streams(params=[stream_name])

        else:
            if stream_name in self.stream_names:
                return('STREAM_[{0}]_ALREADY_EXISTS'.format(stream_name))
            self.stream_names.append(stream_name)

            if self.ws != None and self.socketRunning:
                self.subscribe_streams(params=[stream_name])

                if self.query.split('/')[3] == 'ws':
                    self.set_property(params=['combined',True])

            return({'result':'CREATED_STREAM_NAME', 'stream':stream_name})


    def start(self):
        '''
        This is used to start the socket.
        '''
        if self.socketRunning:
            return('SOCKET_STILL_RUNNING_PLEASE_RESTART')

        ## -------------------------------------------------------------- ##
        ## Here the sockets URL is set so it can be connected to.NO_STREAMS_SET
        logging.debug('[SOCKET_MASTER] Setting up socket stream URL.')
        if self.query == '':
            if self.build_query() == 'NO_STREAMS_SET':
                return('UNABLE_TO_START_NO_STREAMS_SET')
        self.destURL = self.query

        ## -------------------------------------------------------------- ##
        ## Here the 'create_socket' function is called to attempt a connection to the socket.
        logging.debug('[SOCKET_MASTER] Setting up socket connection.')
        self._create_socket()

        ## -------------------------------------------------------------- ##
        # This block is used to test connectivity to the socket.
        conn_timeout = 5
        while not self.ws.sock or not self.ws.sock.connected and conn_timeout:
            time.sleep(5)
            conn_timeout -= 1

            if not conn_timeout:
                ## If the timeout limit is reached then the websocket is force closed.
                self.ws.close()
                raise websocket.WebSocketTimeoutException('Couldn\'t connect to WS! Exiting.')

        self.socketRunning = True
        logging.info('[SOCKET_MASTER] Sucessfully established the socket.')


    def stop(self):

        if self.ws:
            self.ws.close()

        self.socketRunning = False
        self.socketBuffer = {}
        self.ws = None


    def _create_socket(self):
        '''
        This is used to initilise connection and set it up to the exchange.
        '''
        self.ws = websocket.WebSocketApp(self.destURL,
            on_open = self._on_Open,
            on_message = self._on_Message,
            on_error = self._on_Error,
            on_close = self._on_Close,
            on_ping = self._on_Ping,
            on_pong = self._on_Pong)
        
        wsthread = threading.Thread(target=lambda: self.ws.run_forever())
        wsthread.start()


    def _send_message(self, method, params=None):

        message = {'method':method,
                'id':self.id_counter}

        if params != None and params != []:
            message.update({'params':params})

        message = json.dumps(message)

        response_data = self.ws.sock.send(message)

        keys = self.requested_items.keys()

        if len(keys) > self.MAX_REQUEST_ITEMS:
            del self.requested_items[min(keys)]

        self.requested_items.update({self.id_counter:None})
        self.id_counter += 1
        return(self.id_counter)


    def _on_Open(self, wsapp):
        '''
        This is called to manually open the websocket connection.
        '''
        logging.debug('[SOCKET_MASTER] Websocket Opened.')


    def _on_Message(self, wsapp, message):
        '''
        This is used to handle any messages recived via the websocket.
        '''
        try:
            raw_data = json.loads(message)
        except Exception as e:
            print('section 2')
            print(e)
            raw_data = None

        self.last_data_recv_time = time.time()

        if raw_data != None:
            if 'data' in raw_data:
                data = raw_data['data']
            else: 
                data = raw_data

            if 'id' in data:
                if int(data['id']) in self.requested_items:
                    if data['result'] == None:
                        self.requested_items[int(data['id'])] = True
                    else:
                        self.requested_items[int(data['id'])] = data['result']

            if 'e' in data:
                if self.live_and_historic_data:
                    if data['e'] == 'kline':
                        self._update_candles(data)
                            
                    elif data['e'] == 'depthUpdate':
                        self._update_depth(data)

                    else:
                        if 'outboundAccountInfo' == data['e']:
                            self.socketBuffer.update({data['e']:data})
                        elif 'outboundAccountPosition' == data['e']:
                            self.socketBuffer.update({data['e']:data})
                        else:
                            if data['e'] == 'balanceUpdate':
                                pass
                            else:
                                try:
                                    self.socketBuffer.update({data['s']:{data['e']:data}})
                                except Exception as e:
                                    print(e)
                                    print('section 1')
                                    print(raw_data)
                else:
                    self.socketBuffer.update({data['e']:data})



    def _on_Ping(self, wsapp, message):
        '''
        This is called to manually open the websocket connection.
        '''
        logging.debug('[SOCKET_MASTER] Websocket ping.')


    def _on_Pong(self, wsapp, message):
        '''
        This is called to manually open the websocket connection.
        '''
        logging.debug('[SOCKET_MASTER] Websocket pong.')


    def _on_Error(self, wsapp, error):
        '''
        This is called when the socket recives an connection based error.
        '''
        logging.warning('[SOCKET_MASTER] Socket error: {0}'.format(error))


    def _on_Close(self, wsapp, close_status_code, close_msg):
        '''
        This is called for manually closing the websocket.
        '''
        self.socketRunning = False
        logging.info('[SOCKET_MASTER]: Socket closed.')


    def _set_initial_candles(self, symbol, interval, rest_api):
        try:
            hist_candles = rest_api.get_custom_candles(symbol=symbol, interval=interval, limit=self.BASE_CANDLE_LIMIT)
        except Exception as error:
            logging.critical('[SOCKET_MASTER] _initial_candles error {0}'.format(error))
            logging.warning('[SOCKET_MASTER] _initial_candles {0}'.format(hist_candles))
        self.candle_data.update({symbol:hist_candles})


    def _set_initial_depth(self, symbol, rest_api):
        try:
            rest_data = rest_api.get_orderBook(symbol=symbol, limit=self.BASE_DEPTH_LIMIT)
            hist_books = formatter.format_depth(rest_data, 'REST')
        except Exception as error:
            logging.critical('[SOCKET_MASTER] _set_initial_depth error {0}'.format(error))
            logging.warning('[SOCKET_MASTER] _set_initial_depth {0}'.format(rest_data))
        self.book_data.update({symbol:hist_books})


    def _update_candles(self, data):
        rC = data['k']

        live_candle_data = formatter.format_candles(rC, 'SOCK')

        if live_candle_data[0] == self.candle_data[rC['s']][0][0]:
            self.candle_data[rC['s']][0] = live_candle_data

        else:
            if live_candle_data[0] > self.candle_data[rC['s']][0][0]:
                self.candle_data[rC['s']].insert(0, live_candle_data)
                self.candle_data[rC['s']] = self.candle_data[rC['s']][:self.BASE_CANDLE_LIMIT]


    def _update_depth(self, data):
        live_depth_data = formatter.format_depth(data, 'SOCK')

        for lask in live_depth_data['a']:
            if lask[1] in self.book_data[data['s']]['a']:
                if lask[2] == 0.0:
                    del self.book_data[data['s']]['a'][lask[1]]
                    continue

                if self.book_data[data['s']]['a'][lask[1]][0] >= lask[0]:
                    continue

            self.book_data[data['s']]['a'].update({lask[1]:[lask[0],lask[2]]})

        for lbid in live_depth_data['b']:
            if lbid[1] in self.book_data[data['s']]['b']:
                if lbid[2] == 0.0:
                    del self.book_data[data['s']]['b'][lbid[1]]
                    continue

                if self.book_data[data['s']]['b'][lbid[1]][0] >= lbid[0]:
                    continue

            self.book_data[data['s']]['b'].update({lbid[1]:[lbid[0],lbid[2]]})

        all_ask_prices = list(self.book_data[data['s']]['a'].keys())
        all_ask_prices.sort()
        if len(all_ask_prices) > self.BASE_DEPTH_LIMIT+1:
            all_ask_prices_to_cut = all_ask_prices[self.BASE_DEPTH_LIMIT:]
            for aPrice in all_ask_prices_to_cut:
                if aPrice in self.book_data[data['s']]['a']:
                    del self.book_data[data['s']]['a'][aPrice]

        all_bid_prices = list(self.book_data[data['s']]['b'].keys())
        all_bid_prices.sort(reverse=True)
        if len(all_bid_prices) > self.BASE_DEPTH_LIMIT + 1:
            all_bid_prices_to_cut = all_bid_prices[self.BASE_DEPTH_LIMIT:]
            for bPrice in all_bid_prices_to_cut:
                if bPrice in self.book_data[data['s']]['b']:
                    del self.book_data[data['s']]['b'][bPrice]

        
    def _orderbook_sorter_algo(self, books_dict_base, side):
        book_depth_organised = []

        prices_list = list(books_dict_base.keys())

        if side == 'ask':
            prices_list.sort()
        elif side == 'bid':
            prices_list.sort(reverse=True)

        prices_list = prices_list

        for price in prices_list:
            if price in books_dict_base:
                book_depth_organised.append([price, books_dict_base[price][1]])

        return(book_depth_organised)
