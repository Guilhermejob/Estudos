from rest_framework.views import APIView, Response, status
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from movies.models import Movie
from .serializers import MovieOrderSerializer

class MovieOrderView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def post(self, request, movie_id = None):
        
        serializer = MovieOrderSerializer(data = request.data)
        
        serializer.is_valid(raise_exception=True)
        
        get_movie = get_object_or_404(Movie, pk=movie_id)
        
        movie_order = serializer.save(user=request.user, movie = get_movie)
        
        return Response(
                MovieOrderSerializer(movie_order, context={"request": request}).data,
                status=status.HTTP_201_CREATED
            )
        
        
        
        
        
        
        