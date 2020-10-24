def inverte_lista(lista):
    lista2=[]
    x=len(lista)
    while 0<len(lista):
        lista2.append(lista[x])
        x-=1
    return lista2