from math import factorial
def calcula_euler(x,n):
    s = 0 
    x = 1
    for i in range(n+1):
        s+=(x**i)/factorial(i)
    return s
print (calcula_euler)


    
    