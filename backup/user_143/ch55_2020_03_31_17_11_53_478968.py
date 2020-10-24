def encontra_maximo(matriz):
    a=0
    c=len(matriz)
    lista=[]
    while a<c:
        b=0
        y=matriz[a]
        x=len(matriz[a])
        while b<x:
            lista.append(y[b])
            b+=1
        a+=1
    d=0
    w=len(lista)
    while d<w:
        f=1
        g=lista[d]
        k=lista[f]
        while g>k:
            f+=1
            k=lista[f]
        d+=1
    return g
        