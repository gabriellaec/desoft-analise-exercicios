def estritamente_crescente(lista):
    i=0
    p = len(lista)-1
    while i<p:
        d = lista[i+1]-lista[i]
        while d<=0:
            d = lista[i+1]-lista[i]
            del lista[i+1]
        i += 1
    return lista
        