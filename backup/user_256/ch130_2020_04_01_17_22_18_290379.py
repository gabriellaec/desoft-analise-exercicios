def monta_mala(pesos):
    quant = len (int(pesos))
    i= 0
    while i< quant:
        pesos[i]= sum (pesos[i])
        if pesos[i] < 23:
            i +=1
    return pesos

