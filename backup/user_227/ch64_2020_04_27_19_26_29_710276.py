def acha_bigramas(string):
    bigramas=[]
    i=1
    while i<len(string):
        bigrama=string[i-1]+string[i]
        if not bigrama in bigramas:
            bigramas.append(bigrama)
        i+=11
    return bigramas