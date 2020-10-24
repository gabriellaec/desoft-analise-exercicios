def acha_bigramas(string):
    bigramas=[]
    i=0
    while i<len(string)-1:
        bigr=string[i]+string[i+1]
        if not bigr in bigramas:
            bigramas.append(bigr)
        i+=1
    return bigramas