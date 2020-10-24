import math
def calcula_euler(x, n):
    i=2
    while i<n:
        ex = 1 + x
        ex += (x**i)/math.factorial(i)
        i+=1
    return ex