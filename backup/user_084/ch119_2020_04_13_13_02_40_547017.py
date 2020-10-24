import math
def calcula_euler(x,n):
    ex=0
    i=0
    while i<=n:
        ex+=(x**i)/math.factorial(i)
        i+=1
    return ex
        