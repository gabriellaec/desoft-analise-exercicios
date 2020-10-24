def encontra_maximo(lista):
    i=1
    a=lista[0]
    while i<len(lista):
        if lista[i]>a:
            a=lista[i]
        i+=1
    return a