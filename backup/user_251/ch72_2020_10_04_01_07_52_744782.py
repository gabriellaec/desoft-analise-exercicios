def lista_caracteres(a):
    i = 0
    lista = []
    while i < len(a):
        if a[i] not in lista:
            lista.append(a[i])
            i += 1
        else:
            i += 1
        
    return lista