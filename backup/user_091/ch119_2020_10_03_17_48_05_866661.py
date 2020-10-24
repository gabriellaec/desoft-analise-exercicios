import math
def calcula_euler(x,n):
    i=0
    quantidade=0
    while i<n:
        quantidade+=(x**i)/math.factorial(i)
        i+=1
    return quantidade