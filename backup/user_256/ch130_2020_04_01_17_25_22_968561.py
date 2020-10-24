def monta_mala(pesos):
    quant = len(pesos)
    i= 0
    while i< quant:
        if pesos[i] < 23:
            pesos[i]= sum (pesos[i])
            i +=1
        return pesos

