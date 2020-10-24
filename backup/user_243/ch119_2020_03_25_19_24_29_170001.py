import math
def calcula_euler(x,n):
    i=0
    r=0
    while n>i:
        s=x**(i)/math.factorial(i)
        r+=s
        i+=1
    return(r)