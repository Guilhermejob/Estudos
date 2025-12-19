from rest_framework import serializers
from albums.serializers import AlbumSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MusicianSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    instrument = serializers.CharField()
    albums = AlbumSerializer(many=True, required=False)
    
class CustomJWTSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(token)
        token['is_superuser'] = user.is_superuser
        
        return token
    