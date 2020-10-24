def inverte_lista(lista):
    lista_invertida=[]
    for i in range(len(lista)):
        lista_invertida.append(lista[-i])
    return lista_invertida