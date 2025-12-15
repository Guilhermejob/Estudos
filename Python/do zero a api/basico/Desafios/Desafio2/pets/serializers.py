from rest_framework import serializers
from .models import SexOptions, Pet


from traits.serializers import TraitSerializer
from traits.models import Trait


from groups.serializers import GroupSerializers
from groups.models import Group

class PetSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex  = serializers.ChoiceField( choices=SexOptions.choices, default = SexOptions.NOT_INFORMED)
    groups = GroupSerializers(source='group')
    traits = TraitSerializer(many=True)
    
    
    def create(self, validated_data):
        
        # Separamos as chaves group e Traits em variaveis
        group_data = validated_data.pop('group')
        traits_data = validated_data.pop('traits')
        
        # Normalizo o dado para deixar tudo em minusculo e tirar espaços inexistentes
        name = group_data['scientific_name'].strip().lower()
        
        
        # aqui eu crio duas variaveis, pq o metodo get_or_create me retorna 2 valores 1° o objeto que ele achou em banco ou o que ele criou, 2° um booleano se ele criou
        # retorna True se ele foi criado agora,  False e false se ele ja existia,
        # a primeira variavel 'group' vai receber o objeto encontrado ou criado, ja o '_' é uma convenção do python para objeto que 
        # não irei usar, ele ira armazenar o valor Booleano 
        group, _ = Group.objects.get_or_create(
            scientific_name = name
        )
        
        # Aqui eu instancio e crio o pet passando o validated data desconstruido e o group que criamos ou recuperamos do banco acima
        pet = Pet.objects.create(group=group,**validated_data)
        
        # criação de variavel auxiliar que ira comportar 
        traits_pet_data = []
        
        # aqui pegamos a lista de traits retirada do validated_data para fazer um laço de repetição nele 
        for item in traits_data:
            #usamos a mesma lógica que usamos no create acima, caso ele nao exista cria, caso ele exista captura 
            trait, _ = Trait.objects.get_or_create(
                # o .strip() e o .lower() são para garantir a normalização dos dados
                name = item['name'].strip().lower()
            )
            # aqui nos adicionamos o objeto do tipo Trait em uma lista auxiliar
            traits_pet_data.append(trait)
            
            
        # aqui garantimos o vínculo entre os traits (existentes ou recém-criados)
        # e o pet recém-criado, criando os registros na tabela pivô    
        pet.traits.set(traits_pet_data)
        
        return pet
    
    
    def update(self, instance, validated_data):
        
        
        if 'group' in validated_data:
            group_data = validated_data.pop('group')
            name = group_data['scientific_name'].strip().lower()
            group, _ = Group.objects.get_or_create(scientific_name=name)
            instance.group = group
        
        
        if 'traits' in validated_data:
            traits_data = validated_data.pop('traits')
            traits = []
            
            for item in traits_data:
                trait, _ = Trait.objects.get_or_create(
                    name = item['name'].strip().lower()
                )
                
                traits.append(trait)
                
            instance.traits.set(traits)
            
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        
        instance.save()
        return instance
                
