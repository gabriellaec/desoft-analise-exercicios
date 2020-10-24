import math
def calcula_euler(x, n):
    i=0
    resultado=1
    while i<n:
        resultado+=x**i/math.factorial(i)
        i+=1
    return resultado