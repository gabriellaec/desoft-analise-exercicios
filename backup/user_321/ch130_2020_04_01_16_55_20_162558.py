def monta_mala(l):
    i = 0
    mala = []
    while sum(mala) <= 23:
        if sum(mala) + l[0] > 23:
            break
        else:
            mala.append(l[i])
            i +=1
    return mala