def raiz_quadrada(x):
    i=1
    r=0
    continua=True
    while continua:
        l=x-i
        if x<i or l<i:
            continua=False
        else:
            r=r+1
            i=i+2  
    return r
             