def inverte_lista(lista_numeros):
    i=len(lista_numeros)-1
    lista_vazia=[]
    while i >= 0:
        lista_vazia.append(lista_numeros[i])
        i-=1
    return lista_vazia
