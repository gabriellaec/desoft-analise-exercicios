import math
lista=[0]
i=0
while i<n:
    y=(x**i)/math.factorial(i)
    lista.append(y)
    i=i+1
def calcula_euler(x,n):
    e=1+x+sum(lista)
    return e
print(calcula_euler(x, n))
        
        