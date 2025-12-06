lista_1 = list(range(6, 21))
print(lista_1)
lista_1[1] = 'kenzie'
print(lista_1)
print(lista_1[2:5])
lista_1.append('Academy')
print(lista_1)
lista_1.remove('kenzie')
lista_1.remove('Academy')
lista_2 = lista_1[::-1]
print(lista_1)
print(lista_2)
print(len(lista_1), len(lista_2))
lista_1.pop()
lista_2.pop()
print(lista_1)
print(lista_2)
lista_1.clear()
lista_2.clear()
print(lista_1)
print(lista_2)


