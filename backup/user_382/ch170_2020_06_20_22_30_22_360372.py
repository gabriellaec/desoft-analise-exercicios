def apaga_repetidos(string):
    lista = []
    new_string = ''
    for i in string:
        if i not in lista:
            lista.append(i)
            new_string += i
        else:
            new_string += '*'
    return new_string 
        
        