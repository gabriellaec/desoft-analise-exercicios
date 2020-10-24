def mais_frequente(lista):
    d={}
    for i in lista:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    m=0
    palavra=""
    for n, i in d.items():
        if i>m:
            m=i
            palvara=n
    return palavra