def lista_caracteres(x):
    lista = []
    i = 0
    while i < len(x):
        y = x[i]
        if x[i] not in lista:
            lista.append(y)
        i += 1    
    return lista