# Introdução a herança

#Herança em POO é um mecanismo onde uma classe conhecida como filha ou subclasse herda os atributos e metodos de outra classe (conhecida como pai ou superclasse), isso nos permite
#criar classes a partir de classes existentes aproveitando codigo e evitando o DRY

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print('Some generic animal sound')
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species='Dog')
        self.breed = breed
        
    def make_sound(self):
        print('Woof!')
        
    def __str__(self):
        return f'Name: {self.name} - Breed: {self.breed} - Specie: {self.species}'
        
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species='Cat')
        self.breed = breed
        
    def make_sound(self):
        print('Meow!')
        
    def __str__(self):
        return f'Name: {self.name} - Breed: {self.breed} - Specie: {self.species}'
        
dog1 = Dog('Fido', 'Labrador')
print(dog1)
dog1.make_sound()
print('-' * 100)
cat1 = Cat('Tinho', 'Não Especificado')
print(cat1)
cat1.make_sound()

#notaram que as classes dog e cat herdaram herdaram os atributos name e species da superclasse animal e tbm possuem o atributo especifico breed e alem disso as classes 
# cat e dog sobrescrevem o metodo make_sound da super classe animal para implementar o comportamento especifico da subclasse

# No exemplo acima o super().__init__(name, species='dog') é usado para chamar o metodo __ini__ da superclasse animal e passar os argumentos name e species='Dog' no 
# metodo make_sound o super().make_sound() é usado para chamar o metodo make_sound da superclasse e estender o comportamento do metodo
