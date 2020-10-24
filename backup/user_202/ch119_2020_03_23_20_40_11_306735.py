import math 
def calcula_euler(x,n):
    i = 0
    r = 0
    while i > n:
        s = x**(i)/math.factorial(i)
        r = s+r
        i = i+1
    return(r)