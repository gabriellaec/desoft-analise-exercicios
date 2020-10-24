def acha_bigramas(string):
    bigrama = []
    if len(string)>=2:
        i = 0
        while i<len(string):
            bigrama.append(string[i]+string[i+1])
            i += 1
    return bigrama 