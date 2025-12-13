from rest_framework import serializers

class TraitSerializer(serializers.Serializer):
    trait_name = serializers.CharField(source='name')
    id = serializers.IntegerField(read_only = True)
    created_at = serializers.DateTimeField(read_only = True)
    
    
    # Esse método é chamado sempre que o campo trait_name aparece no payload.
    # "value" é o valor bruto enviado pelo cliente.
    # strip() remove espaços no início e no fim, e lower() padroniza o valor para minúsculas.
    def validate_trait_name(self, value):
        return value.strip().lower()