# Paking e Unpacking, Args e Kwargs

#Packing é o processom que permite agrupar varios valores em uma unica variavel, é utilizado para tuplas e listas
a = 1
b = 2
c = 3

packed = a, b, c

print(packed)


#Unpacking é o processo invertido do packing, e quando voce desagrupas os valores de uma unica variavel em varias variaveis

var1, var2, var3 = packed

print(var1, var2, var3)


#args Usado como parametros de função, possibilita que a função receba varios argumentos não nomeados(somente valores)


def show_values(*args: tuple) -> None:
    print(args)
    
print('Primeira chamada de show_values:')
show_values(1, 2, 3)

print('segunda chamada de show_values:')
show_values(4 ,5, 6, 7, 8)


#kwargs mesma coisa que o args mas com valores nomeados (chave-valor)

def show_keywords_values(**kwargs:dict) -> None:
    print(kwargs)
    

print('=' * 50)

print('Primeira chamada de show_keywords_values:')
show_keywords_values(name='Juliana', age=25)

print('Segunda chamada de show_keywords_values:')
show_keywords_values(
    city='Porto Alegre', 
    country='Brasil',
    native_language = 'Gauches'
)



