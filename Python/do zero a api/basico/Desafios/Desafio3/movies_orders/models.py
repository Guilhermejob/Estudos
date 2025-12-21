from django.db import models
from users.models import User
from movies.models import Movie

class MovieOrder(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places = 2) # decimal places vai limitar a quantidade de casas decimais
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_order')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_order')
    