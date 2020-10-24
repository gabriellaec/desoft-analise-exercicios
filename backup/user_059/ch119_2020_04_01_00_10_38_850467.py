import math as m

def calcula_euler(x, n):
    euler = []
    i = 0
    while i<n:
        euler.append(1+x+((x**i)/m.factorial(i)))
        i+=1
    return euler