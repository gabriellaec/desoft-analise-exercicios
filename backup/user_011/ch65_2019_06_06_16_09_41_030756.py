def acha_bigramas(palavra):
    bigramas = []
    i = 0
    while i < len(palavra):
        a = str(palavra[i]) + str(palavra[i+1])
        bigramas.append(a)
        i += 1
    return bigramas