def monta_mala(lista):
    i = 1
    j = 0
    mala = []
    while i <= len(lista):
        mala.append(lista[j])
        if sum(mala) > 23:
            del mala[j]
            break
        i+=1
        j+=1
    return mala