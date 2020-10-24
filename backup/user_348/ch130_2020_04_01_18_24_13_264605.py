def monta_mala (pesos):
    s = 0
    i = 0
    mala = []
    while i < len(pesos):
        s = s + pesos[i]
        i = i + 1
        while s <= 23:
            mala = pesos[i]
    return mala