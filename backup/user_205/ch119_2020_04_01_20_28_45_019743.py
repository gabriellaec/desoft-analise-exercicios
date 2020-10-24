from math import factorial
def calcula_euler(x,n):
    m = 2
    z = 1+x
    while (m<n):
        z += (x**m/factorial(i))
        m+=2
    return z
   