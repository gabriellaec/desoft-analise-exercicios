def acha_bigramas(texto):
    i=0
    bigramas=[]
    while i<len(texto):
        bigrama = texto[i:i+2]
        if bigrama not in bigramas and len(bigrama) == 2:
            bigramas.append(bigrama)
            i+=1
        else:
            i+=1
    return bigramas