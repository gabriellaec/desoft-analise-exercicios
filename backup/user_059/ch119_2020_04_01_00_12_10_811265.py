import math as m

def calcula_euler(x, n):
    euler = []
    i = 1
    while i<n:
        y = m.factorial(i)
        euler.append(1+x+((x**i)/y))
        i+=1
    return euler