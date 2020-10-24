def apaga_repetidos(string):
    lista = []
    new_string = ''
    for i in string:
        if i not in lista:
            lista.append(i)
        else:
            i = '*'
    new_string += i
    return new_string 
        
        