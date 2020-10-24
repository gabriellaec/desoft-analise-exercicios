def raiz_quadrada(x):
    i=1
    r=0
    continua=True
    while continua:
        y=i+2
        if r>0:
            l=x-y
        else:
            l=x-1
        r=r+1
        if l<y:
            continua=False
    return r
             