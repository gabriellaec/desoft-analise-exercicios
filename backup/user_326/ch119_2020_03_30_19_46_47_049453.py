import math
def calcula_euler(x, n):
    i = 0
    eulerx = 0
    while i <= n:
        eulerx = eulerx + (x**i)/math.factorial(i)
        i +=1
    return eulerx