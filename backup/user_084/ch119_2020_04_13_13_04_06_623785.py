import math
def calcula_euler(x,n):
    ex=0
    for i in range(n):
        ex+=(x**i)/math.factorial(i)
    return ex
        