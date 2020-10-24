def raiz_quadrada(x):
    i=1
    r=0
    continua=True
    while continua:
        if x<i or l<i:
            continua=False
        else:
            l=x-i
            r=r+1
            i=i+2  
    return r
             