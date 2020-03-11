def getAuthHeaders(token):
    header = {
        'authorization': 'Bearer ' + token
    }
    return header

def createQuery(params):
    query_params = ["&{}={}".format(key, params[key]) for key in params if params[key]]
    query = ''.join(query_params)
    return query[1:]
