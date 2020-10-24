def zera_negativos(lista):
    c=0
    while c < len(lista):
        if lista[c] < 0:
            lista[c] = 0
        c+=1
    return lista