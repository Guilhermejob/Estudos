from rest_framework.views import APIView, Response, status

from .models import Pet
from rest_framework.pagination import PageNumberPagination
from .serializers import PetSerializer



class PetView(APIView, PageNumberPagination):
    
    
    def post(self, request):
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pet = serializer.save()
        return Response(PetSerializer(pet).data, status=201)
    
    
    def get(self, request, pet_id=None):
         
        #pegando query params por lista
        traits = request.query_params.getlist('traits')
        
        #se tiver query params entra aqui - exemplo de como usar o query params para filtrar uma relação many to many
        if traits:
            
            """
            aqui ele procura tudo que contenha aquele trait
            
            explicação
            
            **** traits -> relacioamento Many to many entre Pet e Trait
            **** __ (double underscore) -> operador do Django ORM para navegar entre relações e acessar campos relacionados
            **** name -> campo da model trait
            **** traits__name -> navega do model Pet para o model Trait através do relacionamento Many-to-Many e acessa o campo name de Trait
            **** __in = traits -> filtra os registros onde o valor do campo name do Trait está contido na lista traits
            """
            
            pet = Pet.objects.filter(traits__name__in = traits).distinct()
            
            result_page = self.paginate_queryset(pet, request, view=self)
            
            serializer = PetSerializer(result_page, many = True)
            
            return self.get_paginated_response(serializer.data)
        
        if pet_id:
            try:
                pet = Pet.objects.get(id = pet_id)
                serializer = PetSerializer(pet)
            except Pet.DoesNotExist:
                return Response({'Message':'Pet not found'}, 404)
            
            return Response(serializer.data, 200)
        
        else:
            pets = Pet.objects.all()
            
            result_page = self.paginate_queryset(pets, request, view=self)
            
            serializer = PetSerializer(result_page, many=True)
            
            return self.get_paginated_response(serializer.data)
        
    def delete(self, request, pet_id=None):
        
        try:
            pet = Pet.objects.get(id = pet_id)
            pet.delete()
        except Pet.DoesNotExist:
            return Response({'Message':'Pet not found'}, 404)
            
        return Response(None, 204)
    
    def patch(self, request, pet_id):
        
        # se tiver o pet id ele encontra no banco
        try:
            pet = Pet.objects.get(id = pet_id)
        # se nao estoura erro 404    
        except Pet.DoesNotExist:
            return Response({'Message':'Pet not found'}, 404)
        
        # serializa o body da requisição usando o PetSerializer, flag partial = True para indicar que pode ter so parte dos campos e nao a totalidade deles
        serializer = PetSerializer(
            pet,
            data=request.data,
            partial = True
        )
        
        # valida o serializer se nao lança excessão
        serializer.is_valid(raise_exception=True)
        
        #salva o pet se o serializer.is_valid for True
        pet = serializer.save()

        return Response(
            PetSerializer(pet).data,
            status=status.HTTP_200_OK
        )        

        
