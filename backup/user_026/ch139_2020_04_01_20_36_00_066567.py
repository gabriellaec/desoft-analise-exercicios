def arcotangente (a,n):
    i=1
    x=0
    if -1<a and a<1:
        while i<=n:
            x = x + a**i/1
            i*=2
            x = x - a**i/i
            i+=2
        return x