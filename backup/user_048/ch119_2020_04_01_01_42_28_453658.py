x=2
n=2
lista=[0]
import math
def calcula_euler(x,n):
    i=0
    while i<n:
        y=(x**i)/math.factorial(i)
        lista.append(y)
        i=i+1
    a=1+x
    e=sum(lista)+a
    return e

        
        