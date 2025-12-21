from rest_framework.views import APIView, Response, status

from .models import Movie
from .serializers import MovieSerializer

from .permissions import IsEmployeeOrReadeOnly


class MovieView(APIView):
    
    permission_classes = [IsEmployeeOrReadeOnly]
    
    def post(self, request):
        

        serializer = MovieSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        

        movie = serializer.save(user = request.user)
        return Response(MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
    
    def get(self, request, movie_id = None):
        if movie_id:
            try:
                movie = Movie.objects.get(pk = movie_id)
                serializer = MovieSerializer(movie)
            except Movie.DoesNotExist:
                return Response({'Message':'O filme não existe'}, status=status.HTTP_404_NOT_FOUND)
            
            
        movies = Movie.objects.all()
        
        serializer = MovieSerializer(movies, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, movie_id = None):
        if movie_id:
            try:
                movie = Movie.objects.get(pk = movie_id)
                movie.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Movie.DoesNotExist:
                return Response({'Message':'O filme não existe'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Message':'Chave movie_id necessaria para a exclusão'}, status=status.HTTP_400_BAD_REQUEST)