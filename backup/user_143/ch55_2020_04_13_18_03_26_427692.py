def encontra_maximo(matriz):
    a=0
    lista=[]
    while a<3:
        b=0
        y=matriz[a]
        while b<3:
            p=y[b]
            lista.append(p)
            b+=1
        a+=1
    f=1
    r=0
    while f<9:
        g=abs(lista[r])
        k=abs(lista[f])
        if g>=k:
            f+=1
        else:
            g=k
    return g
        