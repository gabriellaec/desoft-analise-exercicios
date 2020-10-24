def acha_bigramas(string):
    bigrama=[]
    for z in string:
        x=string[i]+string[i+1]
        if x not in bigrama:
            bigrama.append(x)
    return bigrama