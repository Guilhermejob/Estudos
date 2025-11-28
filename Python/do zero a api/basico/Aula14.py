#Levantamento de exceções

#o levantamento de exceções não tem muito haver com erros e sim com regras de negocio, por exemplo, você esta desenvolvendo um sistema de consultas para um consultorio medico 
# e esse consultorio nao abre as terças feiras, logo, não podem haver consultas marcadas as terças, se alguem marcar, tecnicamente não é um erro, mas uma exceção será levantada
# para que não deixe o cliente marcar consultas as terças

#EX:.
#exessão para evitar valores negativos

def valor_positivo(v):
    if v <= 0:
        raise ValueError('O valor deve ser positivo!')
    return v

#valor_positivo(0)

def somar_valores(a, b):
    try:
        valor_a = valor_positivo(a)
        valor_b = valor_positivo(b)
        print(valor_a, valor_b)
    except ValueError as error:
        print(error.args)
        
somar_valores(1, 2)
somar_valores(1, -1)