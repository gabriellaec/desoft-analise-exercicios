import math
def calcula_euler(x,n):
    e=1
    i=1
    while (i<n):
        i+=1
        e+=e+(x**(i)/math.factorial(i)
    return e 