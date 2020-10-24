def apaga_repetidos(string):
    lista = []
    for i in string:
        if i not in  lista:
            lista.append(i)
        else:
            i.replace('*')
    return string 
        
        