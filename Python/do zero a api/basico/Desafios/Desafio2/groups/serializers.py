from rest_framework import serializers

class GroupSerializers (serializers.Serializer):
    scientific_name = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    
    # Esse método é chamado sempre que o campo scientific_name aparece no payload.
    # "value" é o valor bruto enviado pelo cliente.
    # strip() remove espaços no início e no fim, e lower() padroniza o valor para minúsculas.
    def validate_scientific_name(self, value):
        return value.strip().lower()