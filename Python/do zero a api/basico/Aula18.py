#introdução a classes

#A programação orientada a objetos(POO) é um paradigma no mundo dev que se baseia no conceito de objetos, entidades que representam coisas do mundo real, com seus atributos e
# comportamentos(metodos) na POO objetos são criados apartir de classes, modelos para os objetos e definem seus atributos e comportamentos 


#ex usamos uma convenção que os nomes das classes são feitas em PascalCase, mas os atributos continuam em snake_case, abaixo iremos fazer um exemplo de classe

# class Programador:
#     pass

#INICIALIZADOR
# O metodo __init__ é o metodo especial em python que é chamado automaticamente quando o objeto é criado apartir de uma classe


class Programador:
    # 1. atributo
    languages = ['python', 'nodejs']

    # 2. inicializador
    def __init__ (self, email, telefone):
        # 3. atributos
        self.email = email
        self.telefone = telefone
        
# 1. - Atributo de classe
# 2. - Método Inicializador com os parametros obrigatórios email e telefone
# 3. - Atributos da instancia. São atributos  declarados utilizando a palavra reservada self, sendo uma referencia a instancia atual, similar a o this de outras linguagens

#INSTANCIAS
# uma instancia é um objeto criado a partir de uma classe EX:.

roberto = Programador('roberto@mail.com', '+5544990258742')
claudia = Programador('claudia@mail.com', '+5511912341234')

print(roberto) # >>> <__main__.Programador object at 0x0000026FE1306A50> #Representação padrao de objetos de classe python
print(claudia) # >>> <__main__.Programador object at 0x0000020764DB8A50> #Representação padrao de objetos de classe python

print(roberto.email) # >>> roberto@mail.com
print(claudia.email) # >>> claudia@mail.com

print(roberto.languages) # >>> ['python', 'nodejs']
print(claudia.languages) # >>> ['python', 'nodejs']
