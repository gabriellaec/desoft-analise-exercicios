import math as m

def calcula_euler(x, n):
    euler = []
    i = 0
    y = m.factorial(i)
    while i<n:
        euler.append(1+x+((x**i)/y))
        i+=1
    return euler