import math
def calcula_euler(x,n):
    resultado=0
    i=0
    while i<n:
        termo=x**i/math.factorial(i)
        resultado+=termo
        i+=1
    return resultado
    
    