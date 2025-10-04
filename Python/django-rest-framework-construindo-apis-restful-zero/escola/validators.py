import re
from validate_docbr import CPF

def cpf_invalido(numer_cpf):
    
    cpf = CPF()
    cpf_valido = cpf.validate(numer_cpf)
    
    return not cpf_valido

def nome_invalido(value):
    return not value.isalpha()

def celular_invalido(celular):
    # modelo de numero de celular 51 88888-8888
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return not resposta
