def inverte_lista(lista1):
    a = len(lista1)-1
    lista2=[]
    while a >= 0:
        k = lista1[a]
        lista2.append(k)
        a -= 1
    return lista2