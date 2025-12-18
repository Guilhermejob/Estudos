#adicionando permissoes personalizadas
from rest_framework import permissions
from rest_framework.views import Request, View

class IsAdminOrReadOnly(permissions.BasePermission):
    print('entrou dentro da IsAdminOrReadOnly')
    
    
    def has_permission(self, request: Request, view: View):
        print("AUTH HEADER:", request.headers.get("Authorization"))

        if request.user.is_authenticated and request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return False