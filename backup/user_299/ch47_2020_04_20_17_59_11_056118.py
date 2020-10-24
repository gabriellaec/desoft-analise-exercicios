def estritamente_crescente(lista):
    i = 0
    while i < len(lista):
        d = lista[i+1]-lista[i]
        while d <= 0:
            del lista[i+1]
        i = i+1
    return lista