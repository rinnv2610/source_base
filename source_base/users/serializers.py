from rest_framework import serializers
from source_base.users.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=255)
    password = serializers.CharField(required=True)


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, max_length=255)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)
