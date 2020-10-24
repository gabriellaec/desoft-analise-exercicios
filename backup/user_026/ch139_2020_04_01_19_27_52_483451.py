def arcotangente (a,b):
    i=1
    x=0
    if b<-1 and b<1:
        while i<=b:
            x = x + a**i/i
            i*=2
            x = x - a**i/i
            i+=2
        return x