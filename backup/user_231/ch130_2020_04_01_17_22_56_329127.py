def monta_mala(L=[]):
    while sum(L)>23:
        i= len(L)
        del L[i]
    return L
