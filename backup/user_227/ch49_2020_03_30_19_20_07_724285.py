def inverte_lista(lista):
    invertida = []
    i = len(lista) - 1
    while i > -1:
        invertida.append(lista[i])
        i -= 1
        
    return invertida