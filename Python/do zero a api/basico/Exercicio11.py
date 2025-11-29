def exercicio_1 ():
    notas = [int(input(f'Nota do {i}º bimestre: ')) for i in range(1, 5)]
    return (sum(notas)/len(notas))
  
# print(exercicio_1())

def exercicio_2(n):
    return n * 100

# print(f'{round(exercicio_2(1.80))} cm')

def exercicio_3(n):
    return 2*(n*n)

# print(exercicio_3(7))

def exercicio_4(valor_hora, horas_trabalhadas):
    return(valor_hora*horas_trabalhadas)


# print(exercicio_4(10, 176))

def exercicio_5(n):
    return 5*((n - 32)/9)

# print(round(exercicio_5(85), 2))

def exercicio_6(n):
    return (n *1.8)+ 32

# print(round(exercicio_6(25), 2))

def exercicio_7():
    n1 = int(input('digite um numero inteiro: '))
    n2 = int(input('digite novamente um numero inteiro: '))
    n3 = float(input('digite um numero real: '))
    
    print((n1*2) * (n2/2))
    print((n1*3) + n3)
    print(n3 ** 3)
    
# exercicio_7()

def exercicio_8():
    altura = float(input('digite sua altura em metros: '))
    return (72.7 * altura) - 58

# print(round(exercicio_8(), 2))

def exercicio_9():
    altura = float(input('digite sua altura em metros: '))
    genero = str(input('Qual o seu gênero h = Homem , m = Mulher : '))
    
    if genero == 'h':
        return (72.7 * altura) - 58
    if genero == 'm':
        return (62.1 * altura) - 44.7
    
# print(round(exercicio_9(), 2))

def exercicio_10():
    
    peso  =  float(input('Quantos kilos de pescado tem ?'))
    
    excedente = peso - 50
    
    if excedente > 0:
        multa =  round(excedente * 4, 2)
        
        print(f'A multa que gerou foi de {multa} R$') 

    else:
        print('Não excedeu o peso')

# exercicio_10()

def calculo_de_desconto(salario_bruto, v):

    IR = salario_bruto * v
    salario_liquido = salario_bruto - IR
    print(f'{f"(-) IR ({v*100:.0f}%):":<25} R$ {IR:>10.2f}')
    INSS = salario_bruto * 0.10
    salario_liquido -= INSS
    print(f'{"(-) INSS (10%):":<25} R$ {INSS:>10.2f}')
    FGTS  = salario_bruto * 0.11
    print(f'{"FGTS (11%):":<25} R$ {FGTS:>10.2f}')
    print(f'{"Total de descontos:":<25} R$ {INSS+IR:>10.2f}')
    print(f'{"Salário Líquido:":<25} R$ {salario_liquido:>10.2f}')

def exercicio_11(valor_hora, horas):
    
    descontos = {
        'isento':0,
        'faixa_1': 0.05,
        'faixa_2': 0.10,
        'faixa_3': 0.20
    }
    
    salario_bruto = valor_hora * horas
    
    print(f'{"Salário Bruto:":<25} R$ {salario_bruto:>10.2f}')
    
    if salario_bruto <= 900:
        calculo_de_desconto(salario_bruto, descontos['isento'])
    elif salario_bruto <= 1500:
        calculo_de_desconto(salario_bruto, descontos['faixa_1'])
    elif salario_bruto <= 2500:
        calculo_de_desconto(salario_bruto, descontos['faixa_2'])
    else:
        calculo_de_desconto(salario_bruto, descontos['faixa_3'])
    
            
            
# exercicio_11(15, 220)

# 1 litro cobre 3m quadrados
# cada lata tem 18 litros
# retornar o valor baseado em metros quadrados x quantas latas tera que comprar

# programa devera ler quantos metros quadrados tem que pintar

import math

def exercicio_12(metros):
    quantos_litros = (1*metros)/3
    quantas_latas = math.ceil(quantos_litros/18)
    return f'Você terá que gastar R$ {quantas_latas * 80} em tinta, comprando {quantas_latas} latas de tinta'

print(exercicio_12(300))
        


    