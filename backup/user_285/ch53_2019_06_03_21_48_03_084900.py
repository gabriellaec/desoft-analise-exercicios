def inverte_lista(lista):
    lista_invertida=[]
    i=1
    while i<len(lista)+1:
        lista_invertida.append(lista[-i])
        i+=1
    return lista_invertida