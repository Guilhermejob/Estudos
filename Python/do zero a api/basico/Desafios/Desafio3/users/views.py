from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsEmployeeOrAdminOrReadeOnly
from .models import User
from .serializers import UserSerializer, CustomJWTSerializer
from django.shortcuts import get_object_or_404

class UserView(APIView):
    
    # authentication_classes = []
    permission_classes = [IsAuthenticated, IsEmployeeOrAdminOrReadeOnly]
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, user_id = None):
        

        try:
            user  = get_object_or_404(User ,id = user_id)
            self.check_object_permissions(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message':'User não encontrado'}, status=status.HTTP_404_NOT_FOUND)
            
    def patch(self, request, user_id = None):
        
        try:
            user = get_object_or_404(User, id = user_id)
            self.check_object_permissions(request, user)
        except User.DoesNotExist:
            return Response({'Message':'Usuario não existe'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, request.data, partial=True)
        
        serializer.is_valid(raise_exception=True)
        
        updated_user = serializer.save()
        
        return Response(
            UserSerializer(updated_user).data,
            status=status.HTTP_200_OK
        ) 
        
    
    
                
        
    
class LoginJTWView(TokenObtainPairView):
    serializer_class = (CustomJWTSerializer)
