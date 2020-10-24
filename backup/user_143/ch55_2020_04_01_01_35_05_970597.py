def encontra_maximo(matriz):
    a=0
    c=len(matriz)
    lista=[]
    while a<c:
        b=0
        y=matriz[a]
        x=len(y)
        while b<x:
            lista.append(y[b])
            b+=1
        a+=1
    d=0
    w=len(lista)
    while d<w:
        r=0
        f=0
        g=abs(lista[d])
        k=abs(lista[f])
        while g>=k and f<w:
            k=abs(lista[f])
            f+=1
            r+=1
        if r==w:
            return g
        else:
            d+=1
        