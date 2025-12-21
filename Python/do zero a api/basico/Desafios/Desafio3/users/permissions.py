from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class IsEmployeeOrAdminOrReadeOnly(permissions.BasePermission):
    
    def has_object_permission(self, request:Request, view:View, obj:User):
        
        # Não permite usuario não authenticado
        if not request.user.is_authenticated:
            return False

        # Employee pode tudo(GET e PATCH)
        if request.user.is_employee:
            return True
        
        # Usuario comum só pode acessar o proprio perfil
        if obj == request.user:
            return True
        
        # Qualquer outro caso não é permitido
        return False

        