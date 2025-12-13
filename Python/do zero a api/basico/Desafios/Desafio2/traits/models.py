from django.db import models

class Trait(models.Model):
    name=models.CharField(max_length=20, unique=True)
    pet = models.ManyToManyField('pets.Pet', related_name='traits')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        # normaliza o name removendo espaços extras
        # e padronizando para letras minúsculas antes de salvar
        self.name = self.name.strip().lower()
        return super().save(*args, **kwargs)
    
    class Meta:
        constraints = [
            # Garante que não existam dois registros com o mesmo name,
            # ignorando diferenças entre maiúsculas e minúsculas (case-insensitive)
            models.UniqueConstraint(
                models.functions.Lower('name'),
                name = 'unique_name_ci'
            )
        ]