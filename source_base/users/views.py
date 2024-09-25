from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from source_base.core.utils.response import custom_response
from source_base.users.serializers import RegisterUserSerializer, LoginSerializer
from source_base.users.services import UserService

user_service = UserService()

@swagger_auto_schema(
    method='POST',
    request_body=LoginSerializer,
)
@api_view(['POST'])
def login(request):
    data = user_service.login(request.data)
    return custom_response(data=data)


@swagger_auto_schema(
    method='POST',
    request_body=RegisterUserSerializer,
)
@api_view(['POST'])
def register_user(request):
    data = user_service.register_user(request.data)
    return custom_response(data=data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    data = user_service.get_me(request.user)
    return custom_response(data=data)


