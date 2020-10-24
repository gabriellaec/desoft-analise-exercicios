def monta_mala(lista):
    i=len(lista)-1
    while sum(lista)>23:
        del lista[i]
        i-=1
    return lista