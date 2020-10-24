import math
def calcula_euler(x,n):
    i=1
    c=[1]
    while i<=n:
        a=(x**n)/math.factorial(n)
        c.append(a)
        i+=1
    return(sum(c))