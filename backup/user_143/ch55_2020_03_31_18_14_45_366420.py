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
        g=lista[d]
        k=lista[f]
        while g>k:
            f+=1
            k=lista[f]
            r+=1
        if r==w-1:
            return g
        else:
            d+=1
        