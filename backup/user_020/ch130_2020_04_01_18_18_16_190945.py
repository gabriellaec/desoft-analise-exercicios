def monta_mala(y):
    while sum(monta_mala) > 23:
        del y[-1]
    return y