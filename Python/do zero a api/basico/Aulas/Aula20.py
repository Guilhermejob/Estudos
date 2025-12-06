# Tipos de Metodos

#em python um metodo é uma função que pertence a uma classe ou objeto, e ele é usado para definir o comportamento do objeto ou realizar alguma operação com os atributos do objeto

# Tipos de metodos

# Em python existem 3 tipos de metodos metodos de classe, metodos estaticos e metodos de instancia

#METODOS DE INSTANCIA
# são metodos exclusivos de uma instancia especifica de classe, sendo acessados atraves da instancia eles recebem a instancia como primeiro argumento(self) sendo usado para 
# realizar operações com os atributos da instancia

#METODOS DE CLASSE
# são metodos que recebem a classe como primeiro argumento (conhecido com cls) sendo usados para modificar o estado da classe, eles sao definidos usando a 
# palavra chave @classmethod acima do metodo

#METODO ESTÁTICOS:
# São metodos que não recebem nenhum argumento especial (nem self, nem cls) sendo usados para realizar operações que nao estão relacionadas ao estado da classe ou de uma instancia
# eles são definidos usando a palavra-chave @staticmethod acima do metodo

class MinhaClasse:
    def metodo_de_instancia(self):
        return 'Método de instância chamado'
    
    @classmethod
    def metodo_de_classe(cls):
        return 'Método de classe chamado'
    
    @staticmethod
    def metodo_estatico():
        return 'Método estático chamado'
    
    
#chamando os metodos pela instancia
#instanciando a classe   
obj = MinhaClasse()

print(obj.metodo_de_instancia())
#Método de instância

print(obj.metodo_de_classe())
#Método de classe

print(obj.metodo_estatico())
#Método estático

#Chamando os metodos pela Classe

print(MinhaClasse.metodo_de_classe())
#Método de classe

print(MinhaClasse.metodo_estatico())
#Método estático

# print(MinhaClasse.metodo_de_instancia())
#MinhaClasse.metodo_de_instancia() missing 1 required positional argument: 'self'

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

#niveis de acesso

#o acesso e modificações dos atributos de um objeto ou classe variam conforme o tipo de metodo

"""
--------------------------------------------------------------------------------------------------------------------------------------------
|                    |   Acesso aos Atributos   |   Modificação dos atributos   |   Acesso aos atributos   |   Modificação dos Atributos   |
|    Tipo de Método  |   das instancias da      |   das instancias da classe    |       das classes        |          das classes          |
|                    |         classe           |                               |                          |                               |
|--------------------|--------------------------|-------------------------------|--------------------------|-------------------------------|
|   INSTÂNCIA        |          SIM             |             SIM               |           SIM            |             SIM               |
|--------------------|--------------------------|-------------------------------|--------------------------|-------------------------------|
|   CLASSE           |          NÃO             |             NÃO               |           SIM            |             SIM               |
|--------------------|--------------------------|-------------------------------|--------------------------|-------------------------------|
|   ESTÁTICO         |          NÃO             |             NÃO               |           NÃO            |             NÃO               |
|--------------------|--------------------------|-------------------------------|--------------------------|-------------------------------|

"""

print('-' * 50)
print('*' * 50)
print('-' * 50)



class Student:
    school_name = 'Kenzie'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print('Student', self.name, self.age)
        print('School', self.school_name)
    
    @classmethod
    def show_clasmethod(cls):
        print('School', cls.school_name)
        
    @staticmethod
    def show_staticmethod():
        print('Não tenho acesso aos atributos de classe e nem de instancia')
        
john = Student('John', 17)
john.show()
# Student John 17
# School Kenzie

john.show_clasmethod()
# School Kenzie

john.show_staticmethod()
# Não tenho acesso aos atributos de classe e nem de instancia



print('-' * 50)
print('*' * 50)
print('-' * 50)

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

# Testando modificações que os metodos podem realizar

class Studente_1:
    
    school_name = 'Kenzie'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    # Altera somente o estado do objeto, da classe não altera
    def change_data_instancemethod(self, name, age, school_name):
        self.name = name
        self.age = age
        self.school_name = school_name       
        
    # Altera o estado da classe toda
    @classmethod
    def change_data_classmethod(cls, school_name):
        cls.school_name = school_name
        
    #Não altera nenhum estado
    @staticmethod
    def change_data_staticmethod():
        print('Não tenho acesso aos atributos de classe e nem de instancia')
        
    
guilherme = Studente_1('Guilherme', 29)

print(guilherme.name, guilherme.age, guilherme.school_name)

guilherme.change_data_instancemethod('Gui', 30, 'Kenzie School')

print(guilherme.name, guilherme.age, guilherme.school_name)
print(Studente_1.school_name)

guilherme.change_data_classmethod('Cruzeiro do Sul')

print(guilherme.school_name)
print(Studente_1.school_name)

guilherme.change_data_staticmethod()

#Geralmente acessamos os metodos da classe e metodos estaticos diretamente pela classe

Studente_1.change_data_classmethod('Kenzie Academy Brasil - Escola')
print(Studente_1.school_name)

Studente_1.change_data_staticmethod()


    
        
        
        
    