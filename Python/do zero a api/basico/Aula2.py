#no python para declarar uma string podemos usar aspas simples, duplas ou triplas

minha_string = 'ola recomeço'
minha_string2 = "Sou eu de novo"
minha_string3 = """bora dominar isso logo!!!"""

print(minha_string, minha_string2, minha_string3)

#Mas por convenção sempre usamos a primeira opção, as aspas simples ''

#para fazermos a interpolação de strings em python usamos o f'string' que nada mais é que por o f na frente da string e quando
#quisermos referenciar alguma variavel dentro da string botamos entre chaves {}

#EX:.

#print(f'Valor dentro da variavel minha_string: {minha_string}')

#isso pode ser atribuido a variaveis tambem

minha_string_formatada = f'Valor dentro da variavel minha_string: {minha_string}'

print(minha_string_formatada)

#para representar uma string que ja tem uma aspas dentro dela temos 3 opções

minha_string_com_aspas1 = "eu adoro ir ao McDonald's" #com a string entre aspas duplas e o apóstrofo 
print(minha_string_com_aspas1)
minha_string_com_aspas2 = 'eu adoro ir ao McDonald\'s' #com a string em aspas simples e uma contra barra antes do apóstrofo 
print(minha_string_com_aspas2)
minha_string_com_aspas3 = """eu adoro ir ao McDonald's""" #com aspas triplas e o apóstrofo 
print(minha_string_com_aspas3)

# operações com strings
#concatenação de strings, podemos combinar variaveis do tipo string concatenando elas usando o operador +

string_1 = 'cow'
string_2 = 'boy'

print(string_1 + string_2)

#as strings em python são itens iteraveis, ou seja eu posso acessar cada item individual dela passando o seu indice ex:
print(string_1[0]) #aqui estou acessando o indice 0 da strin_1, ele ira me retornar "c", isso pode ser usado para acessar somente 
                   # um caractere ou percorrer todos os itens da string ex:

for letra in string_1:
    print(letra)
    
#para acessar ao inverso, ou seja de tras para frente podemos usar o indice -1, -2 e por assim em diante ex:
print(string_1[-1])

#fatiamento de strings

#se quisermos um intervalo da string especifico temos que fazer o "fatiamento da string" com a seguinte sintaxe

# nome_da_string[start:stop:step]
# nome_da_string[limite_inferior:limite_superior:passo]

nome_da_string = 'Monty Python'
#aqui por exemplo se eu quisesse extrair apenas a palavra python
#o limite_superior ou o Stop não vai contemplar o valor, ou seja nesse caso o indice 11 seria o 'n' do python, mas como ele nao é
#incluido nós botamos 12 para contemplar o 'n'
print(nome_da_string[6:12]) 

#se quisesse pegar a palavra Monty fariamos assim
print(nome_da_string[:5]) #como o 0 é o inicio da string podemos omitir ele, e no stop sempre por 1 a mais do que queremos pq o ultimo nao e comtemplado

#para o final da string podemos usar a mesma logica, como é o final da string podemos omitir o 12 
print(nome_da_string[6:]) 

#o passo é o equivalente a pular uma casa ou um indice, ou seja se declarar passo 2 para a string teremos algo como MnyPto
print(nome_da_string[:12:2])
#o passo 1 e padrao, ele pegará toda a string, passo 2 pular de 1 em 1, passo 3 de 2 em 2 e assim por diante
#e como fizemos um passo 2 em toda a string podemos omitir o inicio e o fim dela 
print(nome_da_string[::2])

#MANIPULAÇÃO DE STRINGS

#para contarmos quantos caracteres tem nossas strings ao inves de contarmos na mão podemos usar o metodo len e ele retorna a quantidade de caracteres 
print(len(nome_da_string)) #output = 12


#para deixar somente a primeira letra da string em maiusculo usamos o metodo capitalize
string = 'teste de strings'

print(string.capitalize())


#para saber quantas vezes um caractere aparece em uma string ou um conjunto de caracteres aparece usamos o metodo count
print(nome_da_string.count('on')) #output = 2

#para sabermos se uma string inicia ou termina com determinado valor usamos os metodos startswith e endswith

print(nome_da_string.startswith('Mon')) #output = True -> ele retorna um booleano
print(nome_da_string.endswith('Py')) #output = False -> ele retorna um booleano

#para verificar se todo conteudo da string e maiusculo ou minusculo usamos os metodos .islower .isupper

print(nome_da_string.islower()) #output = False -> ele retorna um booleano
print(nome_da_string.isupper()) #output = False -> ele retorna um booleano

#para mudar uma string para tudo maiusculo ou minusculo usamos os metodos .upper ou .lower

print(nome_da_string.upper())#output = MONTY PYTHON
print(nome_da_string.lower())#output = monty python

#para inverter a capitalização das strings usamos o metodo .swapcase ele inverte maiusculo para minusculo e viceversa
teste = 'MiNha StrinG'
print(teste.swapcase()) #output = mInHA sTRINg

#para converter o valor de cada palavra para maiusculo usamos o metodo .title
print(teste.title()) #output = Minha String

#para transformar nossas strings em listas usamos o metodo .split

string_para_lista = teste.split() #caso nao for passado nenhum parametro ele ira reconhecer o espaço como caractere para separar a string em lista 
print(string_para_lista) #output = ['MiNha', 'StrinG']

# se quiser criar uma lista onde cada indice da lista seja um caractere da string temos que usar o list, pq o .split precisa de um parametro para fazer a divisao
minha_string = "Olá Mundo"
lista_de_caracteres = list(minha_string)

print(lista_de_caracteres)

#para substituir um trecho de uma string usamos o .replace
print(nome_da_string.replace('y', 't'))#output = Montt Ptthon

#para centralizar uma string usamos o metodo .center, as vezes quando queremos dar um print e usamos ----------teste----------
#ao inves de escrever isso na mao no print, podemos usar o metodo.center sua sintaxe é assim
# string.center(length, caractere) length é o numero de caracteres para centralizar, e caractere é oque vamos usar, se deixar em branco por padrao o python usa o espaço

sapo = 'Cururu'
print(sapo.center(20, '*'))#output = *******Cururu******* OBS:os 20 caracteres são considerados junto com a string que foi passada
print(len(sapo.center(20, '*'))) #output = 20