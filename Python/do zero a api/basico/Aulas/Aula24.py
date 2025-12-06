# Biblioteca datetime

# A lib datetime em python oferece uma gama de classes para trabalhar com datas e horarios de maneira facil e intuitiva, ela inclui classes para armazenar 
# e manipular informações de data e hora, como ano, mes, dia, hora, minuto, segundo e fuso horario

#EX:.

from datetime import datetime, timedelta


now = datetime.now()

print(type(now)) #<class 'datetime.datetime'>
print(now) #oque retornou quando eu executei >>> 2025-11-30 00:22:20.037509

#Obter informações especificas da data e hora
print(now.year) # 2025
print(now.month) # 11
print(now.day) # 30
print(now.hour) # 0 -> Meia noite
print(now.minute) # 23 
print(now.second) # 51

#Criar uma data e hora especificos


new_year = datetime(2026, 1, 1)
print(new_year)

#calcular a diferença entre duas datas
aniversario = datetime(2026, 3, 25)
diferenca =  aniversario - now
print(diferenca) #  >>> 114 days, 23:31:53.487043

print('-' * 150)
print('*' * 150)
print('-' * 150)

# strftime

# O metodo strftime em python é um metodo que consegue formatar a data e hor de acordo com um formato especifico e retorna uma string com isso

# EX:.
year = now.strftime("%Y")
print(year)

month = now.strftime("%m")
print(month)

day = now.strftime("%d")
print(day)

time = now.strftime('%H:%M:%S')
print(time)

date_time = now.strftime('%d/%m/%Y , %H:%M:%S')
print(date_time)

print('-' * 150)
print('*' * 150)
print('-' * 150)

# strptime

# o metodo strptime é um metodo que é responsavel por fazer um parsing de data e hora, ele é usado para criar um objeto datetime a partir de uma string representando data e hora
# de acordo com um formato especificado

date_string = "30/11/2025"
date_object = datetime.strptime(date_string, '%d/%m/%Y')
print(date_object)

print('-' * 150)
print('*' * 150)
print('-' * 150)


#aqui podemos tambem fazer parse com datetime com hora e tambem com fuso horario

# A lib datetime tambem nos deixa fazer operações matematicas com as datas, mas para isso temos que usar o timedelta para converter um inteiro em um objeto datetime
# EX:.

#Adicionando um dia
print(now + timedelta(days=1))

#subtraindo 60 dias
print(now - timedelta(days=60))

#Adicionando 1 ano
print(now + timedelta(days=365))


#PARAMOS NO BE03-053
#AMANHA DEVEMOS IR ATÉ O 65