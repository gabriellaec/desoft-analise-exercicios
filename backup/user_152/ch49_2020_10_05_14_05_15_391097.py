def inverte_lista (lista):
    invertida = []
    size = len(lista)
    aux = size-1
    i = 0
    while i < size:
        invertida.append(lista[aux])
        aux -= 1
        i += 1
    return invertida