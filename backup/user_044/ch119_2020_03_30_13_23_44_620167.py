import math
lista=[]
i=0
def calcula_euler(x,n):
    n=len(lista)
    if n==0:
        lista[n]=1
    elif n==1:
        lista[n]=1+x
    else:
        while i!=n:
            lista[n]=1+x+(x**n)*(n-1)
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
         
