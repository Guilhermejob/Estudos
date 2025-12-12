from rest_framework import serializers

class AddressSerializer(serializers.Serializer):
    street = serializers.CharField()
    house_number = serializers.CharField()
    city = serializers.CharField()
    zip_core = serializers.CharField()

class AccountSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    sex = serializers.CharField() 
    addresses = AddressSerializer(many=True)
    
    
    """
        source -> é como o dado vai ser "convertido" do serializer para model, por exemplo, se na minha model temos a coluna name, porem no serializer temos user_name
        se passarmos no corpo da requisição como user_name ira ser valido no serializer, porem quando o serializer passar para a model ira der um erro de chave inexistente,
        se fizermos ao contrario, passarmos name o serializer nao vai aceitar pois o campo user_name é obrigatório, usando a propriedade source, garantimos que possamos passar
        user_name para o serializer e a model vai receber como name -> user_name = serializers.CharField(source='name')
        
        read_only = True: isso no serializer vai ser interpretado como um campo de só leitura, ou seja, se passarmos id no corpo da requisição, o serializers irá ignorar e descartar
        ele
        
        write_only = True: campo de só escrita, ele será passado no corpo da requisição, o serializer ira processar ele e fazer todas as operações que usam esse campo, mas na hora
        de devolver a resposta o serializer vai ignorar ele e nao vai retornar no payload da requisição, pq ele é so de escrita e nao permite leitura
        
    
    """
    
       