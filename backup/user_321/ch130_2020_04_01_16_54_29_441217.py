def monta_mala(l):
    i = 1
    mala = []
    while sum(mala) <= 23:
        if sum(mala) + l[i-1] > 23:
            break
        else:
            mala.append(l[i-1])
            i +=1
    return mala