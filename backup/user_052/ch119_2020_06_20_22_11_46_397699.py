import math 
def calcula_euler (x, n):
    i = 2
    while i <= n:
        soma += x**i/math.factorial(i)
        i += 1
    resultado = 1 + x + soma
    return resultado 
        