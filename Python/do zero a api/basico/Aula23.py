# Exceções

# Customizadas/Personalizadas

# em python é possivel criar suas próprias excecoes personalizada derivando da classe Exception ou de alguma de suas subclasses, isso é util quando voce deseja criar
# exceções personalizadas para o seu codigo e retornar uma mensagem de erro significativa para o seu cliente

# EX:.

class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        
def validate_age(age):
    if age < 0:
        raise InvalidAgeError('Age must be positive')
    
try:
    validate_age(-5)
except InvalidAgeError as err:
    print(err.message)

"""
A classe InvalidAgeError é derivada da classe Exception e possui um método __init__ que
recebe uma mensagem de erro. O método validate_age levanta a exceção InvalidAgeError
quando a idade é menor que zero. Mantemos o padrão das exceções nativas do python,
terminando nossa exception customizada com Error. Da mesma forma, utilizamos o raise
para levantá-la seguindo uma condição desenvolvida por nós. No bloco try-except , a
exceção é capturada, e a ela é dada um apelido de err , sendo um objeto da classe
InvalidAgeError . A partir desse objeto, conseguimos acessar o atributo message .

"""

