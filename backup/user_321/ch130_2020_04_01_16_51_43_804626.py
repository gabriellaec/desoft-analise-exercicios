def monta_mala(l):
    i = 0
    mala = []
    while sum(mala) <= 23:
        mala.append(l[i])
        i +=1
    return mala