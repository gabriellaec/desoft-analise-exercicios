from math import factorial

def calcula_euler(x, n):
    euler = []
    i = 0
    while i<n:
        y = factorial(i)
        euler.append(x**i)/y
        i+=1
    return sum(euler)