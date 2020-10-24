def inverte_lista(L):
    i=1
    lista=[]
    while i <= len(L):
        lista.append(L[len(L)-i])
        i+=1
    return lista
    