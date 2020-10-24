def conta_bigramas(string):
    bigramas = []
    for i,s in enumerate(string):
        s = s
        bigrama = string[i:i+2]
        bigramas.append(bigrama)

    contdebi = {}
    for e in bigramas:
        if e in contdebi:
            contdebi[e] = contdebi[e] + 1
        else:
            contdebi[e] = 1
    del contdebi[bigrama]
    return contdebi