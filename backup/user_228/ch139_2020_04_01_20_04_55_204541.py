import math
def arcotangente(x,n):
    i=0
    r=0
    y=0
    while n > i:
        s=x**(i)/i
        r=s+r
        y=r-s
        i=i+1
    return(y)