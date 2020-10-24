import math
def calcula_euler(x,n):
    i=1
    e=0
    while i<n:
        y=(x**(i))/math.factorial(i)
        e=e+y
        i=i+1
  
    return e




        