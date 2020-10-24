lista=[0]
import math
def calcula_euler(x,n):
    i=2
    while i<n-1:
        y=(x**(i))/math.factorial(i)
        lista.append(y)
        i=i+1
    a=1+x
    e=sum(lista)+a
    return e
        