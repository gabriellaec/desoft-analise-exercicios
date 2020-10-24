def inverte_lista(lista):
    lista_invertida=[]
    for i in range(1,len(lista)):
        lista_invertida.append(lista[-i:i-1])
    
    return lista_invertida