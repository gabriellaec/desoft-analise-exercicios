def conta_bigramas(palavra):
    c={}
    i=0
    for letra in range(0,len(palavra),1):
        bigrama = letra[i]+letra[i+1]
        if bigrama in letra:
            c[bigrama]+=1
        else:
            c[bigrama]=1
        i+=1
    return c
print(conta_bigramas('banana'))