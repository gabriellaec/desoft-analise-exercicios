import math
def calcula_euler(x, n):
    i=0
    ex=0
    while i<n:
        ex= ex+(x**i)/math.factorial(i)
        i=i+1
    return ex   