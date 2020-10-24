def acha_bigramas(string):
    bigramas={}
    for i in range(len(string)-1):
        bigramas[string[i:i+2]]= None
    return list(bigramas)
