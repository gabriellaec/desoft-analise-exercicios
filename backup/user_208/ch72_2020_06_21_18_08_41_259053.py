def lista_caracteres (string):
    x = list(string)
    lista = []
    lista1 = []
    i = 0
    while i < len(x):
        if x[i] in lista:
            lista1.append(x[i])
        else:
            lista.append(x[i])
        i+=1
    return lista    
        