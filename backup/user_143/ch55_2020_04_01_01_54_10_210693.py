def encontra_maximo(matriz):
    a=0
    lista=[]
    while a<3:
        b=0
        y=matriz[a]
        while b<3:
            lista.append(y[b])
            b+=1
        a+=1
    d=0
    while d<9:
        r=0
        f=0
        g=abs(lista[d])
        k=abs(lista[f])
        while g>=k and f<=8:
            k=abs(lista[f])
            f+=1
            r+=1
        if r!=8:
            d+=1
        else:
            return g
        