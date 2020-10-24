def monta_mala(lista):
    i = 0
    j = 0
    mala = []
    while j <= len(lista):
        mala.append(lista[i])
        if sum(mala) > 23:
            del mala[i]
            return mala
        i+=1
        j+=1