import math
n=1
fact = 1
  
for i in range(1,n+1): 
    fact = fact * i 

def calcula_euler(x):
    a=1
    i=0

    while i!=19:
        print(a)
        a+=1+x/fact*i
        i+=1