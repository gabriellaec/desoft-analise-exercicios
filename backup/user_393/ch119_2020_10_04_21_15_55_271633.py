import math
def calcula_euler(x,n):
    i=0
    soma=0
    while i<n:
        y=(x**i)/math.factorial(i)
        i+=1
        soma+=y
    return soma

    
        