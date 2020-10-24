def mais_frequente(lista):
    d={}
    for t in lista:
        if t in d:
            d[t]+=1
        else:
            d[t]=1
    m=0
    palavra=""
    for i, t in d.items():
        if t>m:
            m=t
            palvara=i 
    return palavra