from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


def custom_response(data=None, message_code=None, status_code=None):
    response = {
        "meta": {
            "status_code": status_code or HTTP_200_OK,
            "message_code": message_code or "success"
        },
        "data": data or {}
    }
    return Response(response)
