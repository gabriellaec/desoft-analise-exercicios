from math import factorial
def calcula_euler(x,n):
    y = 1 + x
    m = 2
    while (m<n):
        z = (x**m)/factorial(m)
        m+=1
    return y + z