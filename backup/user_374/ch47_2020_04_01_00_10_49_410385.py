
def estritamente_crescente(lista):
    i = 0
    x = len(lista)
    while lista[i] + 1 < x:
        if lista[i] > lista[i+1]:
            del lista[i+1]
        i +=1
    return lista
