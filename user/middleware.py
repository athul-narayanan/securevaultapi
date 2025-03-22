from .utils import _request_local

class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Store request in thread
        _request_local.request = request
        try:
            response = self.get_response(request)
        finally:
            # Clean thread once the request is successfully processed
            if hasattr(_request_local, 'request'):
                del _request_local.request
        return response