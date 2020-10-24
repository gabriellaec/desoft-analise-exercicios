from math import factorial
def calcula_euler(x,n):
    m = 1
    z = 1
    while (m<n):
        z +=  (x**m)/factorial(m)
        m+=1
    return z
   