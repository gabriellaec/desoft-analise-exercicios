def conta_bigramas(palavra):
    bigramas = {}
    for i in range(0,len(palavra)-1):
        bigrama = palavra[i]+palavra[i+1]
        if bigrama not in bigramas:
            bigramas[bigrama]= 1
        else:
            bigramas[bigrama] += 1
    return bigramas