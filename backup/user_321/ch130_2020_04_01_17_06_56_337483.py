def monta_mala(l):
    i = 0
    mala = []
    while sum(mala) < 23:
        if l == []:
            break
        elif sum(mala) + l[i] <= 23:
            mala.append(l[i])
            i +=1
        else:
            break
    return mala
