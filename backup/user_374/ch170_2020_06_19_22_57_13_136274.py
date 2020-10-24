def apaga_repetidos(string):
    lista  = []
    palavra = ''

    for i in string:
        if i not in lista:
           palavra += i
           lista.append(i)
        else:
            palavra += '*'
    
    return palavra