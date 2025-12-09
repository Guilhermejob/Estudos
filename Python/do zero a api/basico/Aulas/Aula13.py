#Tratamento de Exceções

#em pytho quando ocorre um erro o interpretador interrompe a execução do codigo e chama uma exeção associada aquele erro, essas exeções 
#sempre serãod e uma classe que tera seu nome terminado com Error

#ex:
#sum('abc')
# >>>> TypeError: unsupported operand type(s) for +: 'int' and 'str'

#o tratamenti de exeções em payuthon e feito com as palavras chaves try except, o bloco de codigo try e responsavel por envcapsular o codigo
#que pode ferar o erro já o se o codigo der o erro ele pula para o bloco except e ele será executado

try:
    x = 1 / 0
except ZeroDivisionError:
    print('Não é possivel dividir por zero!')
    
#capturando multiplas exceções

#em algumas situações para o mesmo bloco try podem haver erros diferentes que podem ocorrer, e em alguns casos iram precisar de mais de um bloco except para somente
# 1 bloco try

# EX:.

def divide_dois_numeros(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Não é possivel dividir por zero!')
    except TypeError:
        print('Um tipo inválido foi fornecido')
        
divide_dois_numeros(1, 0)

divide_dois_numeros('a', 'b')