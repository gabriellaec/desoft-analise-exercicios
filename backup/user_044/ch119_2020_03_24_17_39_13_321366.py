import math
i=2
y=1+x
def calcula_euler(x,n):
    if n==1:
        y=1
    elif n==2:
        y=1+x
    else:
        while(i!=n):
            i =i+1
            y=y+(x**(n-1))/math.factorial(n-1)
         
