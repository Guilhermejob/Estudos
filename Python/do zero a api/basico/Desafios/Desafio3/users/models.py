from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True, blank=True)
    is_employee = models.BooleanField(default=False)
    
    
    #REGRA DE NEGOCIO
    # Se is_employee = True o superuser tbm será True, caso seja false o superuser tbm sera falso
    # implementado isso no metodo save da model
    

