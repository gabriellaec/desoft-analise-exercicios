import math
def calcula_euler(x, n):
    i=0
    e=0
    while not i==n:
        e=e+(x**(n-1))/math.factorial(n-1)
        i+=1
    return e
        
        
    