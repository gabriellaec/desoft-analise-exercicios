def monta_mala(lista):
    i = len(lista)-1
    while i-1>=0:
        if sum(lista) > 23:
            del(lista[i])
        i -= 1
    return lista