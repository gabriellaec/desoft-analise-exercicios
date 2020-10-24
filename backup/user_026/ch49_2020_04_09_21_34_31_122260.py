def inverte_lista(lista):
    lista_invertida=[]
    for i in lista:
        lista[i]=lista_invertida[len(lista)-1]
    return lista_invertida