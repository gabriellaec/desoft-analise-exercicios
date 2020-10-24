import math
def calcula_euler(x,n):
    i=1
    e=0
    while i!=n+1:
        y=(x**(i-1))/math.factorial(i-1)
        e=e+y
        i=i+1
  
    return e




        