def acha_bigramas(string):
    bigramas=[]
    i=0
    while i<len(string)-1:
        bigramas.append(string[i]+string[i+1])
        i+=1
    return bigramas