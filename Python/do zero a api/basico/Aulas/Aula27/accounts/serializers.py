from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    sex = serializers.CharField()
    
    #aqui podemos Sobrescrever o metodo create do serializer
    def create(self, validated_data:dict):
        return Account.objects.create(**validated_data)