import math
def calcula_euler(x,n):
    soma=1+x
    i=2
    while i<n:
        a=(x**i)/math.factorial(i)
        soma+=a
    return  soma 
    