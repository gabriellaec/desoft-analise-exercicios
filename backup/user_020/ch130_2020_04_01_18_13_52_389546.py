def monta_mala(mala):
    while sum(mala) > 23:
        del mala[i]
    return mala