import threading

_request_local = threading.local()

def get_current_request():
    """
        Get current request from local thread storage
    """
    return getattr(_request_local, 'request', None)

def get_current_user():
    """
        Get the current user from the request
    """
    request = get_current_request()
    if request:
        return request.user
    return None