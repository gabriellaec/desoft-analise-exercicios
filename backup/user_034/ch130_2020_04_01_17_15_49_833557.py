def monta_mala(lista):
    i = 0
    mala = []
    soma = 0
    while i <= len(lista):
        mala.append(lista[i])
        soma += lista[i]
        i+=1
        if soma >23:
            del mala[i]
            return mala
        
        