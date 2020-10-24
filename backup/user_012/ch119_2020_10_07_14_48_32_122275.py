import math
def calcula_euler(x,n):
    soma=0
    i=0
    while i<n:
        soma+=(x**i)/math.factorial(i)
        i+=1
    return soma
    