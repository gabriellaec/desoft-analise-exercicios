import math
def calcula_euler(x, n):
    n=0
    y=1+x+((x**n)/math.factorial(n))
    n=n+1
    y=math.e**x       