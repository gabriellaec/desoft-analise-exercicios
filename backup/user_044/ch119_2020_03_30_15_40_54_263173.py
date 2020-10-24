import math
def calcula_euler(x,n):
    somatoria=0
    i=0
    while i<n:
        somatoria+=(x**i)/math.factorial(i)
        i+=1
    return somatoria


 
         
