from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    username = serializers.CharField(
        validators = [
            UniqueValidator(
                queryset=User.objects.all(),
                message='username already taken'
            )
        ]
    )
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        validators = [
            UniqueValidator(
                queryset=User.objects.all(),
                message='email already registered'
            )
        ]
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(
        required=False,
        allow_null=True
    )
    is_employee = serializers.BooleanField(required=False, default=False)
    
    def create(self, validated_data):
        #aqui ele busca o valor de is_employee, se existir em validate_data ele usa o valor enviado, caso
        #não exista assume False
        is_employee = validated_data.pop('is_employee', False)
        password = validated_data.pop('password')
        
        user = User(**validated_data)
        
        if is_employee:
            user.is_superuser = True
            user.is_staff = True
            user.is_employee = True
        else:
            user.is_superuser = False
            user.is_staff = False
            
        user.set_password(password)
        user.save()

        return user
    
    def update(self, instance : User, validated_data : dict):
        
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.is_employee = validated_data.get('is_employee', instance.is_employee)
        
        instance.save()
        
        return instance
        
    
class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser
        
        return token
    
class LoginSerialzier(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()