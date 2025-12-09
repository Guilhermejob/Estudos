# Métodos especiais

# os metodos especiais são metodos com um nome prefixado e sufixado por duplo sublinhado como __init__ ou __len__ eles sãom usados para implementar operações de alto nivel
# em Python

#UTILIZAÇÃO
# como os metodos especiais ja estão intrisecos nas classe por padrao, podemos sobrescreve-los se quisermos um comportamento diferente. Alguns Exemplos

# __init__

# o metodo especial ou "magico" chamado quando um objeto é criado a partir de uma classe. Ele é usado para inicializar o estado do objeto

"""
class Person:
    def __init__(self, name):
        self.name = name
        
john = Person('John')
print(john.name)
>>> john
"""

# __str___

# é chamado quan do a função str() é aplicada a um objeto ou quando o objeto é usado em uma interpolação de string. Ele é usado para retornar uma string representando o 
# estado do objeto

"""
class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'Classe: {Person.__name__} - Pessoa: {self.name}'
        
john = Person('John')
print(john)
>>> Classe: Person - Pessoa: John

"""

# __str__
# é chamado quando a função len() é aplicada a um objeto. Ele é usado para retornar o tamanho do objeto


# class Person:
#     def __init__(self, name):
#         self.name = name
        
# john = Person('John')
# print(len(john))

#chamando a função len() sem o __len__ declarado em nossa classe retornará um erro TypeError: object of type 'Person' has no len(), para dar certo precisamos declarar o
# metodo __len__ em nossa classe

"""
class Person:
    def __init__(self, name):
        self.name = name
        self.minha_lista = list()
        
    def __len__(self):
        return len(self.minha_lista)
        
john = Person('John')
print(len(john))
>>> 0
"""


