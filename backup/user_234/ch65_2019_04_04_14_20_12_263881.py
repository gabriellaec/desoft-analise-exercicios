def acha_bigramas(texto):
    i=0
    bigramas=[]
    while i<len(texto):
        bigrama = texto[i::2]
        bigramas.append(bigrama)
        i+=1