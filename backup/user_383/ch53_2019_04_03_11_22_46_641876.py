def inverte_lista(lista):
    lista_vazia=[]
    cont=len(lista)
    while cont <= len(lista) and cont>=1 :
        lista_vazia.append(lista[cont-1])
        cont-=1
    return lista_vazia