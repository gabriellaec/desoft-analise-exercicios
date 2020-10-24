def raiz_quadrada(x):
    i=1
    r=0
    continua=True
    if x!=1 and x!= 2:
        while continua:
            l=x-i
            if x<i or l<i:
                continua=False
            else:
                r=r+1
            i=i+2 
    elif x==1:
        r=1
    elif x==2:
        r=2
    return r
             