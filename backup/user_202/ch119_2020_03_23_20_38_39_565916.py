import math 
def calcula_euler(x,n):
    i = 1
    r = 0
    while i > n:
        s = x**(n-1)/math.factorial(n-1)
        r = s+r
        i = i+1
    return(r)