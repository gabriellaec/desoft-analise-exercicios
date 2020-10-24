import math
def calcula_euler(n,x):
    serie=[0]*(n-1)
    serie[0]=1
    serie[1]=x
    a=2
    while a<n:
        serie[a]=(x**a)/math.factorial(a)
        a=a+1
    b=sum(serie)
    return b
    