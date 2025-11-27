meu_dicionario = {'nome':'Kenzinho', 'cidade':'Curitiba', 'Modulo':'M5'}

print(meu_dicionario['nome'])
print(meu_dicionario['cidade'])
print(meu_dicionario['Modulo'])

print(meu_dicionario.get('telefone', 'a chave telefone não existe'))


for chaves in meu_dicionario:
    print(chaves)
    
for chave in meu_dicionario.keys():
    print(meu_dicionario[chave])
    
lista_1 = ['telefone', 'casado', 'idade']
lista_2 = ['999-999-999', False, 28]

d2 = dict(zip(lista_1, lista_2))
print(d2)

meu_dicionario.update(d2)

meu_dicionario.pop('casado')

print(meu_dicionario)

print(meu_dicionario.popitem())

print(meu_dicionario)

meu_dicionario.clear()

print(meu_dicionario)