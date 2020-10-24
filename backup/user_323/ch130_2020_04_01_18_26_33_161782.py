
def monta_mala(lista):
    while sum(lista) > 23:
         S = len(lista)
         del lista[S-1]
    return lista