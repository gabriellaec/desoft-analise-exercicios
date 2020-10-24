def monta_mala(y):
    while sum(y) > 23:
    del y[-1]
    return y