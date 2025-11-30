#Atributos de Classe e Instância

#as classes em python tem 2 tipos de atributos, os de classe e os de instancia

# ATRIBUTOS DE CLASSE

# atributos de classe são atributos que pertencem a classe em si e sao compartilhados por todas as suas instancias da classe, eles são definidos fora do metodo __init__
# e podem ser acessados tanto a partir de classe quanto de instancia 

# ATRIBUTOS DE INSTANCIA

# Atributos de instancia são atributos que são exclusivos da instancia sendo definidos no metodo __init__, eles sao acessados usando o nome_da_instancia seguido do . e o 
# nome do atributo ex:. instancia.name -> aqui estaremos acessando o atributo name da instancia 

class Dog:
    species = "Mammal" # Atributo de classe
    
    def __init__(self, name, breed):
        self.name = name #atributo de instancia
        self.breed = breed #atributo de instancia
    
    def bark(self):
        print('Woof!')
    
    
dog1 = Dog('Fido','Labrador')
dog2 = Dog('Paçoca', 'Vira-Lata')

#acessando atributo de classe via classe
print(Dog.species)

#acessando atributo de classe via instancia
print(dog1.species)
print(dog2.species)

# Acessando atributo de instancia via instancia
print(dog1.name)
print(dog2.name)

# Acessando atributo de instancia via instancia
print(dog1.breed)
print(dog2.breed)

# Tentando acessar atributo de instancia via classe
# print(Dog.name) #AttributeError: type object 'Dog' has no attribute 'name'

#Chamando metodo de classe
dog2.bark()
    
