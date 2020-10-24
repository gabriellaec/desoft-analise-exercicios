def inverte_lista(lista):
    i=0
    lista2=[]
    x=len(lista)
    while i<len(lista):
        lista2.append(lista[x])
        x-=1
        i+=1
    return lista2