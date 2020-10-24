def inverte_lista(lista):
    listainvertida=[]
    posicao=len(lista)-1
    while posicao>=0:
        listainvertida.append(lista[posicao])
        posicao-=1
    return listainvertida