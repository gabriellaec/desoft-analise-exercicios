import math
def calcula_euler(x,n):
    i = 1
    euler = 1
    while i<n:
        numerador = x**i
        denominador = math.factorial(i)
        euler+= numerador/denominador
    return euler