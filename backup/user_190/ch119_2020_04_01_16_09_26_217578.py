import math
def calcula_euler(x, n):
    i=1
    euler=1
    while i<n:
        y=((x**n)/math.factorial(n))
        euler+=y      
        i+=1
    return euler       