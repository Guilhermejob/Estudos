from rest_framework import serializers
from albums.serializers import AlbumSerializer

class MusicianSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    instrument = serializers.CharField()
    albums = AlbumSerializer(many=True, required=False)
    