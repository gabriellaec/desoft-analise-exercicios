def monta_mala(pesos):
    quant = len (pesos)
    i= 0
    while i< quant:
        total= sum (pesos[i])
        if total < 23:
            i +=1
    return total
