def acha_bigramas (texto):
    l1 = []
    for i in range(0,len(texto)-1):
        prox = i+1
        bigrama = [i:prox]
        l1.append(bigrama)
    return l1