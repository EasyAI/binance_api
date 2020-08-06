#! /usr/bin/env python3


import time
import json
import hashlib
import logging
import websocket
import threading
import websocket_api

## sets up the socket BASE for binances socket API.
SOCKET_BASE = 'wss://stream.binance.com:9443'


class Binance_SOCK:

    def __init__(self):
        '''
        Setup the connection and setup data containers and management variables for the socket.
        '''
        self.MAX_REQUEST_ITEMS  = 10
        self.requested_items    = {}


        self.socketRunning  = False
        self.socketBuffer   = {}
        self.ws             = None
        self.stream_names   = []
        self.query          = ''
        self.id_counter     = 0

        ## For locally managed data.
        self.local_manage   = []
        self.candle_update_markets = []
        self.book_update_markets = []
        self.candle_data    = None
        self.book_data      = None

        self.userDataStream_added = False
        self.listen_key = None


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


    ## ------------------ [MANUAL_CALLS_EXCLUSIVE] ------------------ ##
    def subscribe_streams(self, **kwargs):
        return(self._send_message('SUBSCRIBE', **kwargs))

    def unsubscribe_streams(self, **kwargs):
        return(self._send_message('UNSUBSCRIBE', **kwargs))

    def get_current_streams(self):
        return(self._send_message('LIST_SUBSCRIPTIONS'))

    def set_property(self, **kwargs):
        ''' combined = true'''
        print(kwargs)
        return(self._send_message('SET_PROPERTY', **kwargs))

    def get_property(self):
        return(self._send_message('GET_PROPERTY'))


    ## ------------------ [WEBSOCKET_EXCLUSIVE] ------------------ ##
    def set_aggTrade_stream(self, **kwargs):
        return(self.param_check(websocket_api.set_aggTrade_stream, kwargs))


    def set_trade_stream(self, **kwargs):
        return(self.param_check(websocket_api.set_trade_stream, kwargs))


    def set_candle_stream(self, **kwargs):
        return(self.param_check(websocket_api.set_candle_stream, kwargs))


    def set_miniTicker_stream(self, **kwargs):
        return(self.param_check(websocket_api.set_miniTicker_stream, kwargs))


    def set_global_miniTicker_stream(self):
        return(self.param_check(websocket_api.set_global_miniTicker_stream))


    def set_ticker_stream(self, **kwargs):
        return(self.param_check(websocket_api.set_ticker_stream, kwargs))


    def set_gloal_ticker_stream(self):
        return(self.param_check(websocket_api.set_gloal_ticker_stream))


    def set_bookTicker_stream(self, **kwargs):
        return(self.param_check(websocket_api.set_bookTicker_stream, kwargs))


    def set_global_bookTicker_stream(self):
        return(self.param_check(websocket_api.set_global_bookTicker_stream))


    def set_partialBookDepth_stream(self, **kwargs):
        return(self.param_check(websocket_api.set_partialBookDepth_stream, kwargs))


    def set_manual_depth_stream(self, **kwargs):
        result = self.param_check(websocket_api.set_manual_depth_stream, kwargs)
        if result == 'CREATED_STREAM_NAME':
            if websocket_api.set_manual_depth_stream.data_type not in self.local_manage:
                self.local_manage.append(websocket_api.set_manual_depth_stream.data_type)
            if kwargs['symbol'] not in self.book_update_markets:
                self.book_update_markets.append(kwargs['symbol'])

        return(result)


    ## ------------------ [USER_DATA_STREAM_EXCLUSIVE] ------------------ ##
    def set_userDataStream(self, AUTHENTICATED_REST, remove_stream=False):
        if remove_stream:
            message = self.param_check(websocket_api.set_partialBookDepth_stream, {'listenKey':self.listen_key, 'remove_stream':True})
            self.listen_key = None
        else:
            if self.listen_key == None:

                listen_key = AUTHENTICATED_REST.get_listenKey()['listenKey']

                message = self.param_check(websocket_api.set_partialBookDepth_stream, {'listenKey':listen_key})
                self.listen_key = listen_key

                logging.info('SOCKET: Starting local managing')
                lkkaT = threading.Thread(target=self.listenKey_keepAlive, args=(AUTHENTICATED_REST,))
                lkkaT.start()

        return(message)


    def listenKey_keepAlive(self, AUTHENTICATED_REST):
        lastUpdate = time.time()

        while self.listen_key != None:

            if (lastUpdate + 1800) < time.time():
                AUTHENTICATED_REST.send_listenKey_keepAlive(listenKey=self.listen_key)
                lastUpdate = time.time()

            time.sleep(1)


    def param_check(self, api_info, users_passed_parameters=None):
        if 'listenKey' not in users_passed_parameters:
            if api_info.params != None:
                missingParameters = []

                if 'symbol' in users_passed_parameters:
                    base, quote = users_passed_parameters['symbol'].split('-')
                    users_passed_parameters.update({'symbol':(quote+base).lower()})

                if 'R' in api_info.params:
                    for param in api_info.params['R']:
                        if not(param in users_passed_parameters):
                            missingParameters.append(param)

                if len(missingParameters) >= 1:
                    return('MISSING_REQUIRED_PARAMETERS', missingParameters)

                allParams = api_info.params['R'] + api_info.params['O']
                unknownParams = []

                for param in users_passed_parameters:
                    if not(param in allParams):
                        unknownParams.append(param)

                if len(unknownParams) >= 1:
                    return('UNEXPECTED_PARAMETERS', unknownParams)

                stream_name = api_info.endpoint

                for param in allParams:
                    if param == 'local_manager':
                        continue

                    if param in users_passed_parameters:
                        stream_name = stream_name.replace('<{0}>'.format(param), users_passed_parameters[param])
                    else:
                        stream_name = stream_name.replace('<{0}>'.format(param), '')

                if stream_name[-1] == '@':
                    stream_name = stream_name[:-1]

            else:
                if users_passed_parameters != None and users_passed_parameters != {}:
                    return('ENDPOINT_TAKES_NO_PARAMETERS_BUT_SOME_WHERE_GIVEN', users_passed_parameters)

                stream_name = api_info.endpoint
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
        if self.ws != None and self.socketRunning:
            return('SOCKET_STILL_RUNNING_PLEASE_RESTART')

        ## -------------------------------------------------------------- ##
        ## Here the sockets URL is set so it can be connected to.NO_STREAMS_SET
        logging.debug('SOCKET: Setting up socket stream URL.')
        if self.query == '':
            if self.build_query() == 'NO_STREAMS_SET':
                return('UNABLE_TO_START_NO_STREAMS_SET')
        self.destURL = self.query

        ## -------------------------------------------------------------- ##
        ## Here the 'create_socket' function is called to attempt a connection to the socket.
        logging.debug('SOCKET: Setting up socket connection.')
        self.create_socket()

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
        logging.info('SOCKET: Sucessfully established the socket.')


    def stop(self):
        self.ws.close()

        while self.socketRunning:
            time.sleep(0.2)

        self.socketRunning = False
        self.socketBuffer = {}
        self.ws = None


    def create_socket(self):
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


    def _on_Open(self):
        '''
        This is called to manually open the websocket connection.
        '''
        logging.debug('SOCKET: Websocket Opened.')


    def _on_Message(self, message):
        '''
        This is used to handle any messages recived via the websocket.
        '''
        try:
            data = json.loads(message)
        except Exception as e:
            print(e)
            print('json load')

        if 'id' in data:
            if int(data['id']) in self.requested_items:
                if data['result'] == None:
                    self.requested_items[int(data['id'])] = True
                else:
                    self.requested_items[int(data['id'])] = data['result']
                print(data)

        if 'e' in data:
            self.socketBuffer.update({data['e']:data['s']})


    def _on_Ping(self, data):
        '''
        This is called to manually open the websocket connection.
        '''
        logging.debug('SOCKET: Websocket Opened.')


    def _on_Pong(self):
        '''
        This is called to manually open the websocket connection.
        '''
        logging.debug('SOCKET: Websocket Opened.')


    def _on_Error(self, error):
        '''
        This is called when the socket recives an connection based error.
        '''
        print(error)
        print('error')
        logging.warning('SOCKET: {0}'.format(error))


    def _on_Close(self):
        '''
        This is called for manually closing the websocket.
        '''
        print('closed')
        self.socketRunning = False
        logging.info('SOCKET: Socket closed.')