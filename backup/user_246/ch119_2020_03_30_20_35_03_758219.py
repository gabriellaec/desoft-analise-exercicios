import math
def calcula_euler(x, n):
    i=0
    e=0
    while not i==n:
        e=e+(x**n)/math.factorial(n)
        i+=1
    return e
        
        
    