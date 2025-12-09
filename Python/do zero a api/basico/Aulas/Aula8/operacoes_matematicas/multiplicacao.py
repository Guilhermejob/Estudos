from .soma import soma

def multiplicacao (a:int, b:int) -> int:
    acumulador = 0
    
    for i in range(b):
        acumulador = soma(acumulador, a)
    return acumulador