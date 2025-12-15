from django.db import models

class Account(models.Model):
    name = models.CharField()
    email = models.EmailField()
    age = models.IntegerField()
    sex = models.CharField()