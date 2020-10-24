import math

def calcula_euler(x,n):
    i=1
    neperiano=1
    while i<=n:
        neperiano+=(x**i)/math.factorial(i)
        i+=1
    return neperiano