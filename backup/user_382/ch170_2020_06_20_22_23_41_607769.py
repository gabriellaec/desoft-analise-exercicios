def apaga_repetidos(string):
    lista = []
    for i in string:
        if i not in lista:
            lista.append(i)
        else:
            string.replace(i,'*')
    print(string)        
    return string 
        
        