#criar uma função para calcular baskara usando funções builtins
import math

def calculo_delta (a, b, c):
    return pow(b,2) - (4 * a * c)
    
 
def bhaskara (a, b, c): 
    
    resultado_delta = calculo_delta(a,b,c)
    
    if resultado_delta < 0:
        return 'Delta negativo'
    
    raiz_delta = round(math.sqrt(resultado_delta), 2)
    
    x1 = round((-b + raiz_delta) / (2 * a) , 2)
    
    x2 = round((-b - raiz_delta) / (2 * a) , 2)
    
    return f'x1={x1}, x2={x2}'
    

print(bhaskara(7, 3, 4))

print(bhaskara(1, 5, 2))

print(bhaskara(3, 10, 2))