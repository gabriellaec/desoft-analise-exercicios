def monta_mala(l):
    i = 0
    mala = []
    while i in range(len(l)):
        if l == []:
            break
        elif sum(mala) + l[i] <= 23:
            mala.append(l[i])
            i +=1
        else:
            break
    return mala