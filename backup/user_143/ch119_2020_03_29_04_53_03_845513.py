import math
def calcula_euler (x, n):
    i=1
    (math.e)**x=1
    while i<=n:
        (math.e)**x+=(x**i)/(math.factorial(i))
        i+=1
        return math.e**x