def inverte_lista(lista):
    lista_invertida=[]
    for i in range(1,len(lista)):
        lista_invertida.append(lista[-i])
    lista_invertida.append(lista[0])
    return lista_invertida