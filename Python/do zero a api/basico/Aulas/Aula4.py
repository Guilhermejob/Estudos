#Condicionais

#As condicionais são importantes em todas as linguagens de programação pois é com elas para tomar decisoes e controlar
#o fluxo de execução da aplicação de acordo com determinada condição

#sintaxe existem tres estruturas condicionais if, elif e else

#a estrutura if é para verificar se certa determinação e verdadeira ou false

numero = 10

if numero > 0 :
    print('o numero é positivo')
    
    
#ja a estrutura elif é usada para verificar uma segunda condição se a primeira der falso

if numero > 0 :
    print('o numero e positivo')
elif numero < 0 :
    print('o numero é negativo')
    
#a estrutura else é usada para executar um trecho de codigo se todas as outras condições resultaram em false

if numero > 0 :
    print('o numero e positivo')
elif numero < 0 :
    print('o numero é negativo')
else:
    print('o numero é Zero ou inválido')
    

#operadores relacionais

#os operadores relacionais em são usados para comparar valores, eles retornam um valor True ou False dependendo da avaliação da expreção

"""
alguns operadores lógicos em python

== : igualdade (retorna True se os valores forem iguais, False caso contrário)

!= : diferente (retorna True se os valores forem diferentes, False caso contrário)

> : maior que (retorna True se o valor à esquerda for maior que o valor à direita,
False caso contrário)

< : menor que (retorna True se o valor à esquerda for menor que o valor à direita,
False caso contrário)

>= : maior ou igual a (retorna True se o valor à esquerda for maior ou igual ao valor
à direita, False caso contrário)

<= : menor ou igual a (retorna True se o valor à esquerda for menor ou igual ao
valor à direita, False caso contrário)

"""

#alguns exemplos dos operadores em funcionamento 

x = 10
y = 20
print(x == y) # False
print(x != y) # True
print(x > y) # False
print(x < y) # True
print(x >= y) # False
print(x <= y) # True



#operadores lógicos, os operadores logicos ao contrario dos de comparação, nao comparam valores e sim expressoes

"""
alguns operadores logicos em python

and : retorna verdadeiro se ambas as expressões forem verdadeiras
or : retorna verdadeiro se pelo menos uma das expressões for verdadeira
not : inverte o valor lógico da expressão

"""

#Exemplos dos operadores em funcionamento

a = 10
b = 20
c = 30

print(a < b and b < c) # True
print(a < b or b > c) # True
print(not (a == b)) # True