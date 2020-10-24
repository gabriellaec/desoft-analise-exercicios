def estritamente_crescente(lista):
    i=0
    while i<len(lista)-1:
        while lista[i+1]-lista[i]<=0:
            del lista[i+1]
        i += 1
    return lista
        