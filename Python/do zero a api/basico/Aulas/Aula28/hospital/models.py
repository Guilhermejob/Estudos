from django.db import models

class Patient(models.Model):
    
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Medic(models.Model):
    name = models.CharField(max_length=50)
    room = models.CharField(max_length=2)
    
    patient = models.ManyToManyField(Patient, through='hospital.Schedule', related_name='medics') # essa relação nós iremos conseguir acessar os pacientes daquele medico
                                                                                                  # da nossa tabela pivô Schedule      
    
    def __str__(self) -> str:
        return f'{self.name} | {self.room}'
    
class Schedule(models.Model):
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    
#OBS : tambem podemos acessar

# Através do Patient podemos acessar os medicos atraves da chave medics
# Através de Medic podemos acessar Patient atraves da chave patients
# Através de Patient e Medic podemos acessar Schedule
# Atraves da Schedule podemos acessar Patient e Medic