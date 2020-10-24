def monta_mala(mala):
    while sum(monta_mala) > 23:
        del mala[-1]
    return mala