def getAuthHeaders(token):
    """
    Receives a token and returns a header dict
    """
    header = {
        'authorization': 'Bearer ' + token
    }
    return header

def createQuery(params):
    """
    Receives a params dict and build the query string  
    """
    query_params = ["&{}={}".format(key, params[key]) for key in params if params[key]]
    query = ''.join(query_params)[1:]
    return '?' + query if params != [] else query 


def handleShouldBeList(elem):
    """
    Handle if user send a value instead of a list
    """
    if elem:
        elem = elem if isinstance(elem, list) else [elem]
    return elem 