import math
def calcula_euler(x, n):
    euler = 0
    i = 0
    while i < n:
        termo = x**i / math.factorial(i)
        resultado = resultado + termo
        i = i + 1
    return resultado    
    