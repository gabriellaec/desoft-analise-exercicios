def zera_negativos(lista):
    lista = [3,-5,2,-1,8]
    i=0
    while i < len(lista):
        if lista[i] < 0:
            lista[i] = 0
            i= i+1
        else:
            i=i+1
    return lista
    