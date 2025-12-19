from django.db import models
from users.models import User

class RatingChoices(models.TextChoices):
    # Sistema para classificação de idade
    G = 'G' # -> audiencia geral, livre para todos os publicos
    PG = 'PG' # -> Algumas partes não podem ser adequadas para crianças
    PG13 = 'PG-13' # -> algumas partes não podem ser adequadas para crianças abaixo de 13 anos de idade
    R = 'R' # -> Pessoas abaixo de 17 anos de idade devem estar acompanhadas dos pais ou supervisores adultos
    NC17 = 'NC-17' # -> Somente adultos
    
    
class Movie(models.Model):
    title = models.CharField(max_length= 127)
    duration = models.CharField(max_length=10, blank=True, null=True, default='')
    rating = models.CharField(max_length=20, choices=RatingChoices.choices, default=RatingChoices.G)
    synopsis = models.CharField(blank=True, null=True, default='')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')