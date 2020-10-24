def imprime_grade(string):
    digitos = 0
    for i in range(len(string)):
        if string[i].isdigit():
            digitos += 1
    
    return digitos