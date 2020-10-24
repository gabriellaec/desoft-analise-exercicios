def inverte_lista(lista):
    lista_vazia=[]
    cont=len(lista)
    while cont <= len(lista):
        lista_vazia.append(lista[cont])
        cont-=1
	return lista_vazia