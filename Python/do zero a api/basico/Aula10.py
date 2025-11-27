#Tuplas
#Tuplas são como listas, é um tipo de variaval para armazenar varios tipos de dados ao mesmo tempo, mas ao inves dos conchetes as 
# tuplas são representadas por parenteses, e tem uma caracteristica especial a imutabilidade, uma vez declarada e com os dados dentro
# dela ela nunca mais ira poder ser modificada

#sintaxe
minha_tupla = (1, 2, 3, 4, 5)

#para acessar indices de tuplas usamos a mesma mecanica que para acessar indices de listas
print(minha_tupla[0])

#podemos "converter" uma tupla para lista, declarando uma variavel que vai receber a tupla como se fosse uma lista desse jeito

minha_lista = list(minha_tupla)
print(minha_lista)

#por serem imutaveis as tuplas tem apenas 2 metodos

#count, conta o numero de ocorrencias de um determinado valor na tupla
print(minha_tupla.count(4))

#index Recebe um parametro e retorna o primeiro indice em que esse parametro e encontrado, se nao encontrado levanta ValueError

print(minha_tupla.index(5))
