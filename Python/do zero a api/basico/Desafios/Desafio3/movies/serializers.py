from rest_framework import serializers

from .models import RatingChoices, Movie
from users.models import User
from users.serializers import UserSerializer


class MovieSerializer(serializers.Serializer):
    
    id = serializers.CharField(read_only = True)
    title = serializers.CharField()
    duration = serializers.CharField()
    rating = serializers.ChoiceField(choices=RatingChoices.choices, default = RatingChoices.G)
    synopsis = serializers.CharField()
    added_by = serializers.EmailField(
        source='user.email',
        read_only = True
    )
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)