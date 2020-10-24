def acha_bigramas (texto):
    l1 = []
    for i in range(0,len(texto)-1):
        prox = i+2
        bigrama = texto[i:prox]
        l1.append(bigrama)
    return l1