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
    r=0
    while r<9:
        c=0
        f=0
        g=abs(lista[r])
        k=abs(lista[f])
        while f<9:
            if g>k:
                c+=1
            f+=1
        if c==7:
            return g
        else:
            r+=1
        