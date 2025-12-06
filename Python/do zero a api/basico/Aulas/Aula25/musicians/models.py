# As models são como se fossem um esqueleto de como vão ser representadas nossas entidades no banco de dados

from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=30)
    
    class Meta:
        db_table= 'musician'
