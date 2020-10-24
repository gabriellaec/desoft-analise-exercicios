def inverte_lista(lista):
    lista_invertida=[]
    for i in lista:
        lista[i]=lista_invertida[len(lista)-i]
    return lista_invertida
