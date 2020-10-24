def estritamente_crescente(lista):
    i = 0
    lim = len(lista)-1
    while i < lim:
        d = lista[i+1]-lista[i]
        while d <= 0:
            del lista[i+1]
            lim = len(lista)-1
            d = lista[i+1]-lista[i]
        i = i+1
    return lista