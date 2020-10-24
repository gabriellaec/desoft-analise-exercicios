import math
def calcula_euler(x, n):
    i=2
    resultado=1+x
    while i<n:
        resultado+=x**i/math.factorial(i)
        i+=1
    return resultado