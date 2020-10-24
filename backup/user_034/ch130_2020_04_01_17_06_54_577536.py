def monta_mala(lista):
    i = 0
    mala = 0
    while mala <= 23:
        mala = mala + lista[i]
        i+=1
    return mala