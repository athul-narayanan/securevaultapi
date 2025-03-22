# middleware.py
from fileupload.utils import _request_local

class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Store the current request in thread-local storage

        _request_local.request = request
        try:
            response = self.get_response(request)
        finally:
            # Clean up thread-local storage after the request is processed
            if hasattr(_request_local, 'request'):
                del _request_local.request
        return response