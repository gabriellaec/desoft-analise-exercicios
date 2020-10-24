def monta_mala(l):
    i = 0
    mala = []
    while True:
        if l == []:
            break
        elif sum(mala) + l[i] > 23:
            break
        else:
            mala.append(l[i])
            i +=1
    return mala