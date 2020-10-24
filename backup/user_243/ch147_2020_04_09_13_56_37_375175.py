def mais_frequente(lista):
    d={}
    for i in lista:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    m=0
    palavra=""
    for n, t in d.items():
        if t>m:
            palvara=n
    return palavra