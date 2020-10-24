def monta_mala(lista):
    i = 0
    j = 0
    mala = []
    while i <= len(lista):
        mala.append(lista[j])
        if sum(mala) > 23:
            del mala[j]
            return mala
        i+=1
        j+=1