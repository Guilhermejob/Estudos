from django.db import models

class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at= models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # normaliza o nome científico removendo espaços extras
        # e padronizando para letras minúsculas antes de salvar
        self.scientific_name = self.scientific_name.strip().lower()
        super().save(*args, **kwargs)
        
    class Meta:
        
        constraints = [
            # Garante que não existam dois registros com o mesmo scientific_name,
            # ignorando diferenças entre maiúsculas e minúsculas (case-insensitive)
            models.UniqueConstraint(
                models.functions.Lower('scientific_name'),
                name='unique_scientific_name_ci'
            )
        ]
    
    
