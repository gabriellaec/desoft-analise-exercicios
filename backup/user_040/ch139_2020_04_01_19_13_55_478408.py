def arcotangente(x,n):
    r = 3
    f = 1
    a = x
    while f < n:
        if (r+1)%4==0:
            a -= (x**r)/r
            r += 2
            f += 1
        else:
            a += (x**r)/r
            r += 2
            f += 1
    return a
        
        