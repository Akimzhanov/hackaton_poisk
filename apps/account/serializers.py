from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings


from .tasks import send_activation_code


User = get_user_model()


def email_validator(email):
    if not User.objects.filter(email=email).exists():
        raise serializers.ValidationError(
            'User with this email does not exist'
        )
    return email


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(max_length=128, required=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'Username is already, please choose another'
            )
        return username
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Email already in use'
            )
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('password do not match')
        return attrs

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        user.create_activation_code()
        send_activation_code.delay(user.email, user.activation_code)
        return user
        

















    
