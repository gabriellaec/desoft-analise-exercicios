import math
a = [0]*n
def calcula_euler(x, n):
    i=0
    while i<=n:
        a[i] = (x**i)/math.factorial(i)
        i+=1
    y= sum(a)
    return y
