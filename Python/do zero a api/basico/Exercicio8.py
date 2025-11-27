def list_comprehension_exercise_1():
    list = [n for n in range(0, 11)]
    return list

print(list_comprehension_exercise_1())
    


def list_comprehension_exercise_2():
    list = [n for n in range(0, 22) if n % 2 == 0 or n % 3 == 0]    
    return list

print(list_comprehension_exercise_2())

def list_comprehension_exercise_3():
    list = [n for n in range(-5, 32) if n % 2 != 0 and n % 5 != 0]    
    return list

print(list_comprehension_exercise_3())

def list_comprehension_exercise_4():
    list = [n**2 for n in range(0, 11)]
    return list

print(list_comprehension_exercise_4())


def list_comprehension_exercise_5(sentence:str):
    list = [maiuscula for maiuscula in sentence if maiuscula.isupper()]
    return list

print(list_comprehension_exercise_5('O Rato Rui Gosta De QueiJo FresQuiNho'))


def list_comprehension_exercise_6(sentence:str):
    teste = sentence.split(' ')
    comeca_com_r = [palavra for palavra in teste if palavra[0] == 'r']
    return comeca_com_r

print(list_comprehension_exercise_6('o rato rui roeu a roupa do rei de roma'))

