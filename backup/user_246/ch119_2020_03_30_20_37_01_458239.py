import math
def calcula_euler(x, n):
    i=1
    e=0
    while not i==n:
        e=e+(x**(i-1))/math.factorial(i-1)
        i+=1
    return e
        
        
    