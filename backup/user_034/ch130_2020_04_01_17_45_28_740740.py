def monta_mala(lista):
    i = 0
    mala = []
    while i <= len(lista):
        mala.append(lista[i])
        if sum(lista[i]) >23:
            del mala[i]
            return mala
        i+=1
        
        