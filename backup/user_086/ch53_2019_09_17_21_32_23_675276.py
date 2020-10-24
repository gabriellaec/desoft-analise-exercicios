def inverte_lista(lista):
    listainvertida=[]
    posicao=len(lista)
    while posicao>=0:
        listainvertida.append(lista[posicao])
        posicao-=1
    return listainvertida