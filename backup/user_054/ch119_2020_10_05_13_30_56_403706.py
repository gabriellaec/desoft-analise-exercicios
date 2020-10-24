import math
i = 0
E= [0]*n
E[0] = 1
def calcula_euler(x, n):
    while x > 0 and n > 0:
        E[i+1] = (x)**x/math.factorial(x) + i
    return        
   