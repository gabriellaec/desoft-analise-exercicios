def arcotangente (a,b):
    i=1
    x=0
    if -1<b and b<1:
        while i<=a:
            x = x + b**i/i
            i*=2
            x = x - b**i/i
            i+=2
        return x