from math import factorial
def calcula_euler(x,n):
    m = 2
    while (m<=n):
        z = 1 + x + (x**m)/factorial(m)
        return z
    m+=1
print (calcula_euler(2,2))
   