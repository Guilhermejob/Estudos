from rest_framework.views import APIView
from rest_framework.response import Response
from musicians.models import Musician
from rest_framework.pagination import PageNumberPagination
from .serializers import MusicianSerializer

#dois imports abaixo são para permissões nas views
#from rest_framework.permissions import IsAuthenticated #IsAuthenticatedOrReadOnly essa classe funciona para que se o usuario não tiver logado ele só tem permissão de acessar rotas de listagens/leitura/get
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MusicianView(APIView, PageNumberPagination):
    
    # trecho comentado pois configuramos a classe de autenticação globalmente dentro da aplicação, não necessitando configura-la dentro da view
    authentication_classes = [JWTAuthentication] #classes de autenticação
    permission_classes = [IsAdminOrReadOnly] #classes de permissão, no caso do IsAuthenticated o usuario  deverá estar logado para usar os recursos
    
    def post(self, request):
        #aqui iremos pegar o objeto request.data e serializar ele 
        serializer = MusicianSerializer(data = request.data)
        #aqui iremos verificar se o serializer é valido se nao lança exceção
        serializer.is_valid(raise_exception=True)
        musician = Musician.objects.create(**serializer.validated_data)
        #acima estamos usando o unpacking ou seja ele ira quebrar o body nos parametros que temos na model para que o registro seja feito em banc
        serializer = MusicianSerializer(musician)
        return Response(serializer.data, 201)
    
    
    def get(self, request):

        musicians = Musician.objects.all()
        
        result_page = self.paginate_queryset(musicians, request, view=self)
        
        serializer = MusicianSerializer(result_page, many=True)
            
        return self.get_paginated_response(serializer.data)


# class LoginJWTView(TokenObtainPairView):
#     serializer_class = CustomJWTSerializer