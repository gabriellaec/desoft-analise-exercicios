import math

def calcula_euler(x,n):
    i=0
    neperiano=1
    while i<=n:
        neperiano+=(x**n)/math.factorial(n)
        i+=1
    return neperiano