def acha_bigramas(texto):
    bigramas = []
    i = 0
    while i < len(texto) - 1:
        if not (texto[i]+texto[i+1]) in babador:
            bigramas.append(texto[i]+texto[i+1])
            i+=1
        else:
            i+=1
    return bigramas