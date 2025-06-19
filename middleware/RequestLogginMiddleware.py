from typing import Any
from tracker.models import RequestLog

class RequestLogging:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        request_info = request

        RequestLog.objects.create(
            request_info = vars(request_info),
            request_type = request_info.method,
            request_method = request_info.path,
        )
        print()
        return self.get_response(request)
    
