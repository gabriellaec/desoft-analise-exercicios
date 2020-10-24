import math

def calcula_euler(x,n):
    i=0
    neperiano=0
    while i<=n-1:
        neperiano+=(x**i)/math.factorial(i)
        i+=1
    return neperiano