def inverte_lista(lista):
    i=0
    listas=[]
    while(i<len(lista)):
        listas.append(lista[-i])
        if(lista[i]<0):
            del lista[i]
        return lista
    i+=1