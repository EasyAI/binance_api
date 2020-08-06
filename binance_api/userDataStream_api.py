class get_listenKey:
    params = None
    method = 'POST'
    endpoint = '/api/v3/userDataStream'
    security_type = 'USER_STREAM'


class send_listenKey_keepAlive:
    params = {'R':['listenKey']}
    method = 'PUT'
    endpoint = '/api/v3/userDataStream'
    security_type = 'USER_STREAM'


class close_listenKey:
    params = {'R':['listenKey']}
    method = 'DELETE'
    endpoint = '/api/v3/userDataStream'
    security_type = 'USER_STREAM'