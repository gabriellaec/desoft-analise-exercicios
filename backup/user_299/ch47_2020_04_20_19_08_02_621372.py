def estritamente_crescente(lista):
    d = 1
    for i,e in enumerate(lista):
        if i+1 <= len(lista):
            d = lista[i+1]-lista[i]
            while d <= 0:
                del lista[i+1]
    return lista