def conta_bigramas(palavra):
    c={}
    i=0
    for letra in range(0,len(palavra)-1):
        bigrama = palavra[i]+palavra[i+1]
        if bigrama in c:
            c[bigrama]+=1
        else:
            c[bigrama]=1
        i+=1
    return c