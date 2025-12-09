#Comprehensions

#comprehensions são uma forma de criar listas, dicionarios e conjuntos, ela permite realizar loop e transformação de elementos
# em uma unica linha, sem precisar escrever varias linhas para tal

#O list comprehension é um loop for em uma única linha, onde a expressão armazenará os valores. Aqui estão alguns 
# exemplos de comprehensions em Python:

numbers = [1, 2, 3, 4, 5]
squares = []

#no metodo "Tradicional"
for n in numbers:
    squares.append(n**2)

print(squares)

# Com List comprehension
squares_comprehension = [n**2 for n in numbers]

print(squares_comprehension)

#podemos fazer condicionais dentro do list comprehension
#para fazermos uma condicional ou filtragem dentro de list comprehensions temos 2 formas uma mais simples com epenas uma condicional
#outra mais complexa que encorpa uma condicional else

#para filtrar paresm sem list comprehensions
evens = []
odds = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)
        
print(evens)

#com list comprehensions
evens_comprehensions = [n for n in numbers if n % 2 == 0]

print(evens_comprehensions)

#dict comprehension
lista = ['Brasil', 'Argentina', 'Chile']

novo_dict_comprehensions = {
    indice:pais for indice, pais, in enumerate(lista)
}

print(novo_dict_comprehensions)

