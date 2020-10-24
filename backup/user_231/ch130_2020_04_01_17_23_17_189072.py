def monta_mala(L=[]):
    while sum(L)>23:
        i= len(L)
        del L[i-1]
    return L
