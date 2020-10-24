import math
def calcula_euler(x,n):
    i=0
    
    lista=[0]
    while i<n:
        y=(x**(i))/math.factorial(i)
        lista.append(y)
        e=sum(lista)
        i=i+1
  
    return e
        