def inverte_lista(lista):
    lista2=[]
    x=len(lista)-1
    while 0<=x:
        lista2.append(lista[x])
        x-=1
    return lista2