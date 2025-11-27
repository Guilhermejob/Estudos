def sum_numbers (*args):
    total = 0
    for i in args:
        total += i
        
    return total
        

numbers = [1, 2, 3, 4, 5, 6]

print(sum_numbers(*numbers))


def get_multiplied_amount(multiplier, *numbers):
    total = 0
    for i in numbers:
        total += i * multiplier
    return total

numbers = [1, 2, 3]
multiplier = 2

print(get_multiplied_amount(multiplier, *numbers))

def word_concatenator(*words):
    frase = ''
    
    for palavra in words:
        frase += f'{palavra} '
        
    return frase


words = ["Tá", "pegando", "fogo", "bicho!!!"]

print(word_concatenator(word_concatenator(*words)))


words = ["eae", "amigão", "belezinha?"]

def teste (*args):
    nova_frase = ''
    for palavra in reversed(args):
        for letra in reversed(palavra):
            nova_frase += letra
        nova_frase += ' '
    return nova_frase
    

print(teste(*words))


def dictionary_separator(**kwargs):
    teste = tuple(kwargs.keys())
    teste_2 = tuple(kwargs.values())
    return teste,teste_2

user = {"name": "Naruto", "age": 16, "favorite word": "IchirakuRamen"}

items = dictionary_separator(**user)

print(type(items))

print(items[0])
print(items[1])

def dictionary_creator(*args, **kwargs):
    indice = 0
    new_dict = {}
    
    for key, value in kwargs.items():
        for item in args:
            new_dict[args[indice]] = value
        indice += 1
            
    return new_dict
    
change_keys = ["username", "password", "address"]
user = {"name": "Williams", "some_key": "1234"}

modified_user = dictionary_creator(*change_keys, **user)
print(modified_user)

def purchase_logger(**kwargs):
    return f'{kwargs['quantity']} {kwargs['name']} bought by {kwargs['price']}'
    
purchase = {"name": "washing powder", "price": 6.7, "quantity": 4}
purchase_log = purchase_logger(**purchase)
print(purchase_log)
    
    
# "4 washing powder bought by 6.7"