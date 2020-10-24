def inverte_lista(lista):
    i=0
    invertida=[0]*lista
    while i<len(lista):
        invertida[-i]=lista[i]
    return invertida