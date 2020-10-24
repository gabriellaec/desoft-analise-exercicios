import math
lista=[]
i=0
def calcula_euler(x,n):
    somatoria=0
    while i<n:
        somatoria+=(x**i)/math.factorial(i)
  		i+=1









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
    return y        
         
