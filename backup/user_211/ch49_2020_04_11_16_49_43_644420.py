def inverte_lista(lista):
    i=0
    invertida=[0]*len(lista)
    while i<len(lista):
        invertida[-i-1]=lista[i]
        i+=1
    return invertida