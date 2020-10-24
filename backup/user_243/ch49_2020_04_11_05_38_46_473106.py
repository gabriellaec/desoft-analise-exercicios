def inverte_lista(lista):
    lista2=[]
    x=len(lista)-1
    while 0<=len(lista)-1:
        lista2.append(lista[x])
        x-=1
    return lista2