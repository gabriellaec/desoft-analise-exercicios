def inverte_lista(lista):
    lista2=[]
    i=1
    while i<len(lista):
        lista2.append(lista[-1-i])
        i+=1
    return lista2