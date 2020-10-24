def acha_bigramas(string):
    bigramas = []
    i = 0
    while i < len(string) - 1:
        if not string[i]+string[i+1] in lista:
            bigramas.append(string[i]+string[i+1])
        i = i + 1
    return bigramas