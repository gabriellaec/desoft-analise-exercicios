import math
def calcula_euler(x, n):
    i=0
    l=2
    d=2
    soma=0
    if n==1:
        e=1
    elif n==2:
        e=1+x
    else:
        while i<n-2:
            soma=soma+(x**l)/math.factorial(d)
            l+=1
            d+=1
            i+=1
            e=1+x+soma
    return e