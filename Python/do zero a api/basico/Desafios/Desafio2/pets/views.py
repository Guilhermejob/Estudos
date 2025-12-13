from rest_framework.views import APIView, Response

from .models import Pet
from groups.models import Group
from rest_framework.pagination import PageNumberPagination
from .serializers import PetSerializer
from groups.serializers import GroupSerializers


class PetView(APIView, PageNumberPagination):
    def post(self, request):
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pet = serializer.save()
        return Response(PetSerializer(pet).data, status=201)
    
    def get(self, request):
        
        pets = Pet.objects.all()
        
        result_page = self.paginate_queryset(pets, request, view=self)
        
        serializer = PetSerializer(result_page, many=True)
        
        return self.get_paginated_response(serializer.data)
        
