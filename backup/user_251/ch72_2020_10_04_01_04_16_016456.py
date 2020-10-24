def lista_caracteres(a):
    i = 0
    lista = []
    while i < len a and a[i] not in lista:
        lista.append(a[i])
        i += 1
        
    return lista