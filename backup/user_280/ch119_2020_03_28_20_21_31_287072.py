import math

def calcula_euler(x, n):
    a = [0]*n
    i=0
    while i<=n:
        a[i] = (x**i)/math.factorial(i)
    i+=1
    y= sum(a)
    return y
