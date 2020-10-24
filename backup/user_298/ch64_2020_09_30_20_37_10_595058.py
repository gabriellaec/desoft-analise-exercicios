def acha_bigramas(palavra):
    t = 0
    bigramas = []
    while t < (len(palavra)-1):
        bigrama = palavra[t]+palavra[t+1]
        if bigrama not in bigramas:
            bigramas.append(bigrama)
        t += 1
    return bigramas