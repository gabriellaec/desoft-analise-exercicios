def raiz_quadrada(x):
    i=1
    r=0
    continua=True
    while continua:
        if x<i:
            continua=False
        l=x-i
        if l<i:
            continua=False
        r=r+1
        i=i+2  
    return r
             