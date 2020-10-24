def raiz_quadrada(x):
    i=1
    r=0
    continua=True
    while continua:
        y=i
        l=x-y
        if l<y:
            continua=False
        r=r+1
        i=i+2  
    return r
             