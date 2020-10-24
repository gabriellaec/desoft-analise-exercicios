def acha_bigramas(palavra):
    bigramas = []
    for i in range(len(palavra)):
        bi = palavra[i:i+2]
        if bi not in bigramas:
            bigramas.append(bi)
    return bigramas