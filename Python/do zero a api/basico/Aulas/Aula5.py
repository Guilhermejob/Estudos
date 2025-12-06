#Estruturas de repetição

# loopings ou estrutura de repetiçoes são usadas para repetir varias vezes determinado bloco de instruções
# existem 2 estruturas de repetições for e while

#FOR

#sintaxe -> for elemento in iteravel -> repete o bloco para cada item o iteravel passado como parametro
#sintaxe -> for i in range (1, 6) -> repete o bloco para o intervalo descrito desconsiderando o ultimo

teste = '******'

#imprime cada elemento da lista
for elemento in [1, 2, 3, 4, 5, 6]:
    print(elemento)
    
print(teste.center(50, '-'))
    
for i in range (1, 6):
    print(i)
    
print(teste.center(50, '-'))

for caractere in 'olá mundo':
    print(caractere)
    
#o loop while ira executar um bloco de código enquanto uma expressão for verdadeira

print(teste.center(50, '-'))
i = 1

while i <= 5:
    print(i)
    i += 1
    
print(teste.center(50, '-'))
#auxiliares podemos usar o comando break para interromper um laço de repetição antes da condição ser verdadeira 
# ou o continue  para interromper a iteração atual e continuar em seguida

#interrompe quando o i for igual a 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)
 
print(teste.center(50, '-'))
#quando o i for igual a 3 ele interrompe pulando o 3 e continua com o loop em seguida    
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    