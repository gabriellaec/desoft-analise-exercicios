import math
def calcula_euler(x,n):
    euler = 1
    expoente = 1
    while expoente < n:
        euler = euler + (x**expoente) / math.factorial(expoente) 
        expoente += 1
    return euler