import math
def calcula_euler(x, n):
    i=1
    while i<n:
        y=((x**n)/math.factorial(n))
        y=math.e**x       
        i+=1