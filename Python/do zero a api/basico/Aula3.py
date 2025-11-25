"""
as funções são trechos de codigo ou instruções que realizam uma tarefa especifica e 
podem ser chamadas em algum lugares diferentes do código, podendo serem reutilizaveis
tornando o codigo mais legivel e de mais facil manutenção
"""

#sintexe

def minha_funcao(arg1, arg2):
    return arg1 + arg2

resultado = minha_funcao(1, 2)

print(resultado) # output = 3

"""
as funções sempre vão ter a mesma sintaxe a palavra chave def seguida do nome da função e seus parametro em parenteses se tiver e dois pontos,
em seguida vai para proxima linha escrever as instruçoes sempre identando corretamente

alem disso podemos por argumentos opcionais em nossas funções setando um argumento padrao assim se nao passarmos ele vai assumir
o valor padrao como no exemplo abaixo

"""

def minha_funcao2 (arg1, arg2 = 2):
    return arg1 + arg2

resultado = minha_funcao2(3)

print(resultado)# output = 5

#Auxiliar pass, usamos muito quando estamos marcando algo para uma implementação futura ou para suprimir o erro "SyntaxError: unexpected EOF while parsing"

# cria uma função vazia
def minha_funcao():
    pass
# cria uma função vazia da mesma forma
def minha_funcao2():
    ...

# cria um loop vazio
for x in range(10):
    pass
# cria uma classe vazia
class MinhaClasse:
    pass

#as funções builtins são funções ja imbutinas no python, podendo somente chamar elas passar os parametros quando necessario e a utiliza-las

#ex: função sum()  soma valores passados como parametros, sempre tendo que passsar um iteravel, como uma lista ou tuplas, tendo
# 2 parametros, o iteravel e um valor de inicio(opcional) em que ele começa a somar com aquele valor ja guardado

tupla_para_somar = (1, 2, 3)

print(sum(tupla_para_somar, 2)) # output = 8