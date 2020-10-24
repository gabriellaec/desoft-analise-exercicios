def conta_bigramas(palavra):
    bigramas = {}
    for i and e in palavra:
        if not i and e in bigramas:
            bigramas[i+e] = 1
        else:
            bigramas[i+e] +=1
    return bigramas