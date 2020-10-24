import math
def calcula_euler(x,n):
    i=0
    c=[]
    while i<=n:
        a=(x**i)/math.factorial(i)
        c.append(a)
        i+=1
    return(sum(c))