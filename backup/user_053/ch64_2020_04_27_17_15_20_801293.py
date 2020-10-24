def acha_bigramas(palavra):
    bigramas = []
    lista = []
    for i in range(0, len(palavra) - 1):
        bigrama = palavra[i: i+2]
        bigramas.append(bigrama)
    i = 0
    while i < len(bigramas):
        j = 0
        while j < len(bigramas):
            if bigramas[i] == bigramas[j] and i != j:
                del(bigramas[j])
            j += 1
        i += 1
    return bigramas