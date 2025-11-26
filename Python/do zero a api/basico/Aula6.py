#LISTAS
#lista nos permitem armazenar um conjunto de elementos em uma unica variavel, listas são mutaveis, então depois de criada podemos manipula-la

"""
listas são muito versateis, podem conter varios elementos e de qualquer tipo, incluindo numeros, strings, listas entre outros
para criar uma lista em python basta nomea-la e atribuir seus conteudos entre conchetes separados por virgula
"""

minha_lista = [3, 'abacate', 9.7, [4, 5, 6]]
print(minha_lista[3])

#utilizando funções builtins para criar listas
minha_lista_builtin =  list('abc')
print(minha_lista_builtin)

#OBS, no segundo metodo de criar listas funciona apenas para valores iteraveis, aqui foi criado uma lista apartir de uma string
#por que a string e um objeto iteravel se tentarmos com (123) daria um erro
"""
teste = list(123)
File "...Estudos\Estudos\Python\do zero a api\basico\Aula6.py", line 19, in <module>
    teste = list(123)
TypeError: 'int' object is not iterable
"""

#FATIAMENTO

#assim como usamos o fatiamento em string podemos usar em listas tambem

lista = ['1', 'teste', '3']

print(lista[0])
print(lista[2])
print(lista[-1])
print(lista[:2])
print(lista[0:3:2]) #[:3:2] ou [::2]

carrinho_de_compras = ['Banana', 'Pera', 'Tomate']

for item in carrinho_de_compras:
    print(item)
    
    
    
#no python existem diversos metodos uteis para manipularmos nossas listas

"""
list.append(x) adiciona elemento no final da lista
list.extend(iteravel) adiciona todos os itens de outro iteravel no final da lista
list.insert(i, x) insere o elemento x na posição i da lista
list.remove(x) remove o item cujo o valor é igual a x
list.pop([i]) remove o elemento na posição i ou o ultimo se i nao for especificado
list.clear() remove todos os itens da lista
list.index(x[, start[, end]]) retorna o indice do primeiro valor igual a x, tambem consegue determinar um intervalo nas funções start e end
list.count(x) retorna o numero de vezes que o elemento x aparece na lista
list.sort(key = None, reserve=False) classifica os itens em order crescente (ou descrescente se o reserve for True)
list.reverse() inverte a ordem das listas


"""
