def lista_caracteres(str):
    lista = []
    i = 0
    while i<len(str):
        lista.append(str[i])
        i += 1
    while k<len(lista):
        if lista.count(lista[k]) > 1:
            del(lista[k])
        k += 1
    return lista
