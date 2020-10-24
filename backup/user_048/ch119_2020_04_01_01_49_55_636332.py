lista=[0]
import math
def calcula_euler(x,n):
    i=1
    while not i==n+1:
        y=(x**(i-1))/math.factorial(i-1)
        lista.append(y)
        i=i+1
    a=1+x
    e=sum(lista)+a
    return e




        