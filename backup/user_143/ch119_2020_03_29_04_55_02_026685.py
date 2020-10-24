import math
def calcula_euler (x, n):
    i=0
    while i<=n:
        (math.e)**x+=(x**i)/(math.factorial(i))
        i+=1
        return (math.e)**x