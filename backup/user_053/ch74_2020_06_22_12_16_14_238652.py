def conta_bigramas(string):
    pares = {}
    bigramas = []
    for i in range(0, len(string)-1):
        big = string[i] + string[i+1]
        bigramas.append(big)
    for bigs in bigramas:
        if bigs not in pares.keys():
            pares[bigs] = 1
        else:
            pares[bigs] += 1
    return pares