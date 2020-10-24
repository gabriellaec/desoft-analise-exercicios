import math
def calcula_euler(x,n):
    sum = 1 + x
    i = 2
    while(i < n):
        i+= 1
        sum+= (x**i)/math.factorial(i)
        
    return sum 
        