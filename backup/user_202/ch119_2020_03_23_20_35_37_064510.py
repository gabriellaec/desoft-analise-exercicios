import math 
def calcula_euler(x,n):
    i = 0
    while i > n:
        s = x**n/math.factorial(n)
        r = s+r
        i = i+1
    return(r)