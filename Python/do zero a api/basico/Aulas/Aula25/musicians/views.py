from rest_framework.views import APIView
from rest_framework.response import Response
from musicians.models import Musician
from rest_framework.pagination import PageNumberPagination
from .serializers import MusicianSerializer


class MusicianView(APIView, PageNumberPagination):
    
    
    def post(self, request):
        #aqui iremos pegar o objeto request.data e serializar ele 
        serializer = MusicianSerializer(data = request.data)
        
        #aqui iremos verificar se o serializer é valido se nao lança exceção
        serializer.is_valid(raise_exception=True)
        
        
        
        musician = Musician.objects.create(**serializer.validated_data)
        #acima estamos usando o unpacking ou seja ele ira quebrar o body nos parametros que temos na model para que o registro seja feito em banco

        serializer = MusicianSerializer(musician)
        
        return Response(serializer.data, 201)
    
    def get(self, request):
        musicians = Musician.objects.all()
        
        result_page = self.paginate_queryset(musicians, request, view=self)
        
        serializer = MusicianSerializer(result_page, many=True)
            
        return self.get_paginated_response(serializer.data)