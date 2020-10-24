import math
def arcotangente(x,n):
    i=1
    r=0
    y=0
    while n > i:
        s=x**(i)/i
        r=s+r
        y=r-s
        i=i+2
    return(y)