def arcotangente (a,n):
    i=1
    x=0
    if -i<a and a<i:
        while i<=n:
            x = x + a**i/i
            i*=2
            x = x - a**i/i
            i+=2
        return x