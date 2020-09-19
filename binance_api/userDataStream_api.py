class get_listenKey_spot:
    params = None
    method = 'POST'
    endpoint = '/api/v3/userDataStream'
    security_type = 'USER_STREAM'


class send_listenKey_keepAlive_spot:
    params = {'R':['listenKey']}
    method = 'PUT'
    endpoint = '/api/v3/userDataStream'
    security_type = 'USER_STREAM'


class close_listenKey_spot:
    params = {'R':['listenKey']}
    method = 'DELETE'
    endpoint = '/api/v3/userDataStream'
    security_type = 'USER_STREAM'


class get_listenKey_margin:
    params = None
    method = 'POST'
    endpoint = '/sapi/v1/userDataStream'
    security_type = 'USER_STREAM'


class send_listenKey_keepAlive_margin:
    params = {'R':['listenKey']}
    method = 'PUT'
    endpoint = '/sapi/v1/userDataStream'
    security_type = 'USER_STREAM'


class close_listenKey_margin:
    params = {'R':['listenKey']}
    method = 'DELETE'
    endpoint = '/sapi/v1/userDataStream'
    security_type = 'USER_STREAM'