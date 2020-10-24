def acha_bigramas(x):
    l=[]
    for i in range(len(x)-1):
        bigrama=x[i:i+2]
        if bigrama not in l:
            l.append(bigrama)
    return l
