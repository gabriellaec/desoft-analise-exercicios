def estritamente_crescente(lista):
    i=0
    while i<len(lista)-1:
        d = lista[i+1]-lista[i]
        while d<=0:
            d = lista[i+1]-lista[i]
            del lista[i+1]
        i += 1
    return lista
        