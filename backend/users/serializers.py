from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import logging

logger = logging.getLogger(__name__)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta: 
        model = User
        fields = ('email', 'username', 'password', 'password_confirm')
        extra_kwargs = {
            'password': {'write_only': True},
            'password_confirm': {'write_only': True}
        }

    def validate(self, data):
        logger.info(f'Validating data: {data}')

        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        logger.info('Passwords match.')
        return data
    
    def create(self, data):
        logger.info(f'Creating user in RegistrationSerializer with data: {data}')
        
        try:
            user = User.objects.create_user(
                email=data['email'],
                username=data['username'],
            )
            user.set_password(data['password'])
            user.save()
            logger.info(f'User created: {user}')
            return user
        except Exception as e:
            logger.error(f'Error creating user: {e}')
            raise 
    
class LoginSerializer(TokenObtainPairSerializer):
    pass