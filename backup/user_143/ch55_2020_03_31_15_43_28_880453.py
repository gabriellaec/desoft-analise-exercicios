def encontra_maximo(matriz):
    a=0
    b=0
    c=len(matriz)
    lista=[]
    while a<c:
        y=matriz[a]
        x=len(matriz[a])
        while b<x:
            lista.append(y[b])
            b+=1
        a+=1
    d=0
    f=1
    w=len(lista)
    while d<w:
        g=lista[d]
        k=lista[f]
        while g>k:
            f+=1
        d+=1
    return g
        