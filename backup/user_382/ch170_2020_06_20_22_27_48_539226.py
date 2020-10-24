def apaga_repetidos(string):
    lista = []
    new_string = 0 
    for i in string:
        if i not in lista:
            lista.append(i)
        else:
            i = '*'
        new_string += i
    return string 
        
        