def raiz_quadrada(x):
    i=1
    r=0
    continua=True
    while continua:
        y=i+2
        l=x-y
        r=r+1
        if l<y:
            continua=False
    return r
             