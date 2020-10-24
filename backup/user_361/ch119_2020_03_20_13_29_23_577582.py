import math
def calcula_euler(x,n):
    sum = 1 + x
    i = 2
    while(i < n):
        sum+= (x**i)/math.factorial(i)
        i+= 1
    return sum 
        