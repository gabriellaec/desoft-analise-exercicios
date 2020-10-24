import math
def calcula_euler(x, n):
    i=1
    ex = 1
    while i<n:
        ex = 1
        ex += (x**i)/math.factorial(i)
        i+=1
    return ex