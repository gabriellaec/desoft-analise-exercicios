import math
i = 0

def calcula_euler(x, n):
    while x > 0 and n > 0:
        i = (x)**x/math.factorial(x) + i
    return        
   