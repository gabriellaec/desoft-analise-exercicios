def acha_bigramas(palavra):
    bigramas = []
    i = 1
    while i < len(palavra):
        a = str(palavra[i - 1]) + str(palavra[i])
        if a not in bigramas:
            bigramas.append(a)
        i += 1
    return bigramas