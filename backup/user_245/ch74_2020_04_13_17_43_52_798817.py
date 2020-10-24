def conta_bigramas(palavra):
    bigramas = {}
    for i in palavra:
        if not i in bigramas:
            bigramas[i] = 1
        else:
            bigramas[i] +=1
    return bigramas