from django.db import transaction
from rest_framework_simplejwt.tokens import RefreshToken

from source_base.users.models import User
from source_base.users.serializers import RegisterUserSerializer, UserSerializer


class UserService:

    @staticmethod
    def login(req_data):
        user = User.objects.get(email=req_data.get("email"))

        if user.check_password(req_data.get("password")):
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

        return {
            'message': 'Email or password incorrect',
        }

    @staticmethod
    def register_user(req_data):
        with transaction.atomic():
            serializers = RegisterUserSerializer(data=req_data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return req_data

    @staticmethod
    def get_me(user):
        serializers = UserSerializer(user, many=False)
        return serializers.data
