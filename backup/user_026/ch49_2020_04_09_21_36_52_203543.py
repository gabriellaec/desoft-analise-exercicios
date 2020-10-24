def inverte_lista(lista):
    lista_invertida=[]
    i=0
    while i<len(lista):
        lista[i]=lista_invertida[len(lista)-i]
        i+=1
    return lista_invertida
