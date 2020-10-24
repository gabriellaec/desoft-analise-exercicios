import math
def calcula_euler (x,n):
    i = 0
    r = 0
    while n > i:
        y = x**(i)/math.factorial(i)
        r = y + r
        i = i + 1
        
        return (r)
        