import math
def arcotangente(x,n):
    i=1
    r=0
    y=0
    while n > i:
        s=x**(i)/math.factorial(i)
        r=s+r
        i=i+2
    return(math.asin(r))