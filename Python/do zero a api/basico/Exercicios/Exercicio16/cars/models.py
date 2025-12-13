from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField(max_length=4)
    is_avaliable = models.BooleanField(default=True)
    
