def inverte_lista(lista):
    lista2=[]
    x=len(lista)
    while 0<=len(lista)-1:
        lista2.append(lista[x-1])
        x-=1
    return lista2