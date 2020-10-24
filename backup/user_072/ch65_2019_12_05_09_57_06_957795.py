def acha_bigramas(string):
    bigrama=[]
    i=0
    while i<len(string)-1:
        x=string[i]+string[i+1]
        if x not in bigrama:
            bigrama.append(x)
        i+=1
    return bigrama