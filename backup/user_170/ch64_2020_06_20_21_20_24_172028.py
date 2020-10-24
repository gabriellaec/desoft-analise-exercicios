def acha_bigramas(palavra):
    bigramas = []
    palavra = str(palavra)
    for i in range(len(palavra)):
        bi = palavra[i:i+2]
        if not bi in bigramas:
            bigramas.append(bi)
    return bigramas