#DICIONARIOS

#dicionarios em python são uma estrutura de dados que permite armazenar pares de valores-chaves de forma organizada, cada item
# de um dicionario é determinardo por uma chave e um valor

#para criar um dicionario em Python basta nomea-lo como se fosse uma variavel e na atribuição determinar suas chaves e valores,
#entre chaves e separados por virgula, como o exemplo abaixo

meu_dicionario = {
    'nome': 'Guilherme',
    'idade': 29,
    'cidade':'Charqueadas'
}

#OBS, as chaves sempre são entre aspas

#existem varios meios de manipular esses dicionarios

#acessando valor de um dicionario é semelhante a acessar um indice de array, mas ao inves de pormos o numero do indice entre conchetes
#nos botamos a chave que queremos acessar

# Por exemplo se quisermos acessar o nome do nosso objeto acima vamos fazer assim
print(meu_dicionario['nome'])

#para adicionarmos uma nova chave e valor no dicionario fazemos assim
meu_dicionario['profissao'] = 'Programador'

#chamamos a variavel ao lado a chave que queremos adicionar e adicionamos o valor a ela

print(meu_dicionario)

#para atualizar um valor fazemos algo semelhante a adicionar uma valor, chamamos o objeto, ao lado a chave que queremos editar e em seguida
# o novo valor a ser atribuido

meu_dicionario['cidade'] = 'Porto Alegre'
print(meu_dicionario)

#para remover uma chave valor de um dicionario existem alguns metodos
#del meu_dicionario['profissao'] # ira deletar a chave profissão
#print(meu_dicionario)
#meu_dicionario.pop('idade') #ira excluir a chave idade 
#print(meu_dicionario)

#para atualizar varios valores de um objeto usamos o metodo update

meu_dicionario.update({'modulo':'M5', 'cidade':'Joinville', 'idade':30}) 
# se por uma chave e valor que nao existe até então no objeto o metodo update cria eles
print(meu_dicionario)


#METODO GET
#para acessar uma chave valor tambem temos o metodo get

print(meu_dicionario.get('idade'))

#o metodo get aceita um segundo parametro, nos passamos ele para que ele retorne algo se nao acharmos a chave e valor
print(meu_dicionario.get('Senioridade', 'Chave não encontrada'))

#looping
#Existem varios meios de percorrermos um objeto em python aqui em baixo estao alguns exemplos


#percorre somente as chaves do dicionario e as imprime

for chave in meu_dicionario:
    print(chave) 
    
for chave in meu_dicionario.keys():
    print(chave)
    
#percorre as chaves do dicionario e as usa para imprimir os valores
for chave in meu_dicionario:
    print(meu_dicionario[chave])
 
 
#percorre os items do dicionario imprimindo pares de chave-valor   
for chave, valor in meu_dicionario.items():
    print(f'{chave}:{valor}')