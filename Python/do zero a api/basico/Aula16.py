#Conjuntos

#conjuntos assim como na matematica é um conjunto de objetos ou membros como são tipicamente mencionados 
#EX:.
# x tal que x é par e x é maior que 4 e menor que 10
#A = { x | x é par e 4 < x < 10}
# O conjunto acima pode ser definido dessa forma
# A = {6, 8}

# X tal que 2x mais um é igual a 7 e x é um inteiro
# B = { x | 2x + 1 = 7 e x é inteiro}
# o conjunto acima pode ser representado dessa forma
# B = {3}

#ja em python conjuntos ou set é uma coleção não ordenada e sem elementos duplicados de valores imutaveis, os conjuntos são usados para armazenar varios valores e permitir
#operações de conjunto, com união, interseção e diferença

#para criar um conjunto usamos a palavra set em seguida uma lista de elementos entre chaves, ou usar a declaração literal usando ({})

# meu_conjunto = set([1, 2, 3, 4, 5, 5, 5, 4])

# print(meu_conjunto)

"""
principais metodos de conjuntos

set.add(elemento): Adiciona um elemento
set.remove(elemento): Remove um elemento, se ele não encontrar lança um erro
set.discard(element): Remove um elemento, se ele não encontrar não lança um erro
set.clear(): Remove todos os elementos do conjunto
set.copy(): Cria uma cópia do conjunto
set.update(conjunto): Adiciona todos os elementos de um conjunto ao conjunto atual
set.intersection(conjunto): Retorna um novo conjunto com os elementos que estao presentes em ambos os conjuntos
set.difference(conjunto): Retorna um novo conjunto com os elementos que estao presentes no primeiro conjunto, mas nao estão presentes no segundo conjunto
set.union(conjunto): Retorna um novo conjunto com os elementos presentes em ambos os conjuntos
set.isdisdjoint(conjunto): Retorna True se os conjuntos não tiverem elementos em comum, caso contrario retorna False
"""

meu_conjunto = set ([1, 2, 3, 4, 5])


meu_conjunto.add(6)
print(meu_conjunto)

meu_conjunto.remove(3)
print(meu_conjunto)

# meu_conjunto.discard(7) #não lança erro
# meu_conjunto.remove(7) #lança erro

outro_conjunto = meu_conjunto.copy()
print(outro_conjunto)

meu_conjunto.update([7, 8, 9])
print(meu_conjunto)

conjunto_a = set([1, 2, 3])
conjunto_b = set ([2, 3, 4])

#Cria um novo conjunto com os elementos em comum entre os conjuntos
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)

#Cria um novo conjunto com os elementos presentes no conjunto_a mas nao presentes em conjunto_b
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)

#Cria um novo conjunto com todos os elementos presente em ambos os conjuntos
uniao = conjunto_a.union(conjunto_b)
print(uniao)

#verifica se os conjuntos não tem elementos em comum
sao_disjuntos = conjunto_a.isdisjoint(conjunto_b)
print(sao_disjuntos)