import math
def calcula_euler (x, n):
    i=0
    while i<=n-1:
        ((math.e)**x)=(x**i)/(math.factorial(i))+(x**(i+1))/(math.factorial(i+1))
        i+=1
        return (math.e)**x