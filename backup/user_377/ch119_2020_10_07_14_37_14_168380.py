import math
def calcula_euler(x, n):
    euler = 0
    i = 0
    while i < n:
        termo = x**i / math.factorial(i)
        euler = euler + termo
        i = i + 1
    return euler    
    