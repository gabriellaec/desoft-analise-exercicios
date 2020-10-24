from math import factorial
def arcotangente(x,n):
    m = 3
    i = 3
    while (m<n):
        y = x - (x**m)/i + (x**m+2)/i+2
        m+=2
        i+=2
    return y