import math
def arcotangente(x,n):
    i = 0
    exp = 1
    div = 1    
    pos = 0
    neg = 0
    while i < n:
        if i%2 == 0:
            pos = pos + (x**(exp)/div)
        if i%2 == 1:
            neg = neg + (x**(3*exp)/div+2) 
        div+=2
        exp+=2
        i +=1
    arc = (pos - neg)*(math.pi/180)
    return arc