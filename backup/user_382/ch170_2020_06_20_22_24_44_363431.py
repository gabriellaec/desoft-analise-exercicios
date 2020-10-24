def apaga_repetidos(string):
    lista = []
    for i in string:
        if i not in lista:
            lista.append(i)
        if i in lista:
            string.replace(i,'*')      
    return string 
        
        