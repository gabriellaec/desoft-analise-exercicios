def inverte_lista(lista):
    lista_invertida=[]
    for i in lista:
        lista[1]=lista_invertida[len(lista)-1]
    return lista_invertida