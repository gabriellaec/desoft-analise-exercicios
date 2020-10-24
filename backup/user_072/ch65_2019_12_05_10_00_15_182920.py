def acha_bigramas(string):
    bigrama=[]
    for i in str(string):
        x=string[i]+string[i+1]
        if x not in bigrama:
            bigrama.append(x)
    return bigrama