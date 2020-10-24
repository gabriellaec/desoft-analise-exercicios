from math import factorial
def calcula_euler(x,n):
    s = 0 
    for i in range(n):
        s+=(x**i)/factorial(i)
    return s



    
    