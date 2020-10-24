def conta_bigramas(palavra):
    bigramas = {}
    for i in range(len(palavra)-1):
        if not i in bigramas:
            bigramas[palavra(i:i+2)] = 1
        else:
            bigramas[palavra(i:i+2)] +=1
    return bigramas