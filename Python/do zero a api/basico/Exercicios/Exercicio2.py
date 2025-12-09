def corresponding_parenthesis(a):
    parenthesis_list = list(a)
    parenthesis1 = []
    parenthesis2 = []
    
    
    for parenthesis in parenthesis_list:
        if parenthesis == '(':
            parenthesis1.append(parenthesis)
        if parenthesis == ')':
            parenthesis2.append(parenthesis)
    
    if len(parenthesis1) > len(parenthesis2):
        result = parenthesis1[len(parenthesis2) :]
    else:
        result = parenthesis2[len(parenthesis1) :]
            
    
    return "".join(result)
    
    
print(corresponding_parenthesis("()()"))
print(corresponding_parenthesis("()))"))
print(corresponding_parenthesis(")))((((("))



def remove_more_than_two_repetitions(text: str):
    response = []
    response.append(text[0])
    response.append(text[1])

    for index, char in enumerate(text[2:], 2):
        if text[index - 1] != char or text[index - 2] != char:
            response.append(char)

    return "".join(response) 
            
            
print(remove_more_than_two_repetitions("Ollloco meuuuu, taaa peegaando fogoo biiiiichooo"))
