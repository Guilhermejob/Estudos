#python usa padrão snake case para nomeação de variaveis e funções
# ex: id_usuario, cobrança_nao_processada

#isso é um comentario em 1 linha

"""
isso é um comentario em multiplas linhas

tambem pode ser usado para criar docstrings, comentarios que podem ser atribuidos
a documentação de algum metodo, classe ou função
"""

"""
os tipos primitivos em python são

1. String (str)
2. Inteiro (int)
3. Decimal (float)
4. Booleano (bool)
5. Vazio (NoneType)
"""

#declaração de variavel
minha_string = 'hello'

#verificando o tipo da variavel
print(type(minha_string)) # output: <class 'str'>

meu_inteiro = 123
print(type(meu_inteiro)) # output: <class 'int'>

meu_decimal = 3.1415
print(type(meu_decimal)) # output: <class 'float'>

meu_booleano = True
print(type(meu_booleano)) # output: <class 'bool'>

meu_vazio = None
print(type(meu_vazio)) # output: <class 'NoneType'>

MINHA_CONSTANTE = 'Ola Python' # em python para declarar uma constante usamos letras maiusculas em tudo, isso nao indica que 
                               # a variavel é imutavel, mas indica que não podemos altera-la 
                               
#tipagem dinaminca

minha_string = '2'
print(type(minha_string)) #no python o tipo da variavel é inferido automaticamente conforme o valor atribuido a ela


#tipagem forte

#O Python não converte automaticamente o tipo dos objetos, por exemplo se tentarmos somar o valor de uma variavel int com 
#uma variavel do tipo string ele vai dar um type error

meu_numero = 1
#soma = meu_numero + minha_string  # int + string = TypeError

#definindo funções
def minha_funcao():
    #em python a identação faz o papel das chaves em javascript, então a identação que define o escopo de funções, loops e classes
    meu_valor = 1234
    return meu_valor

print(minha_funcao())

