def arcotangente(x,n):
    i=1
    a=0
    while i <= n:
        arco=(1**a)-((x**i)/i)
        i+=2
        a+=1
    return arco