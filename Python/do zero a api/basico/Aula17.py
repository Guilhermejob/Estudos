#Copia rasa e copia profunda

#Copia rasa é quadno copiamos apenas os valores de uma variavel para outra, sem sua referencia na memoria

#EX:.
list_1 = [1, 2, 3]
list_2 = list_1.copy()

print(f'Lista 1: {list_1}')
print(f'Lista 2: {list_2}')

print(f'local na memoria list1: {id(list_1)}') #local na memoria list1: 2384529678592
print(f'local na memoria list2: {id(list_2)}') #local na memoria list2: 2384529827456

#Não possuem o mesmo espaço em memoria
print(list_1 is list_2)

# Possuem o mesmo valor
print(list_1 == list_2)

#Copias profundas
#nas copias profundas novos objetos são criados, porem diferente das copias rasas, as copias profundas criam referencias para elementos mutaveis internos do objeto original

list_original = [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6]
list_copy = list_original.copy()

#alterando os elementos dentro de list_copy
list_copy[0] = 10
list_copy[3][0] = 'Z'

print(list_original)   #[1, 2, 3, ['Z', 'b', 'c'], 4, 5, 6]
print(list_copy)       #[10, 2, 3, ['Z', 'b', 'c'], 4, 5, 6]

#repare que nos prints que fizemos mostra que mudança que fizemos no primeiro elemanto não refletiu na lista original, porem a que fizemos na lista ['a', 'b', 'c'] teve reflexo
#tanto na list copy quanto na original isso se da por que a referencia de ['a', 'b', 'c'] nao foi copiada com o list_copy, portanto o copy() gera copias rasas, ou seja ela cria
#referencias para objetos internos

#PARA QUE ISSO NAO OCORRA MAIS podemos usar a função deepcopy() da biblioteca copy

import copy

list_original_1 = [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6]
list_copy_1 = list_original.copy()
list_copy_1[3][0] = 'Z'

print(list_original_1)   #[1, 2, 3, ['a', 'b', 'c'], 4, 5, 6]
print(list_copy_1)       #[1, 2, 3, ['Z', 'b', 'c'], 4, 5, 6]

#note agora que a auteração que fizemos em list_copy_1 nao refletiu em list_original_1
