import math

def calcula_euler(x, n):
    e_resultado = 0
    for i in range(n):
        e_resultado += x**i/math.factorial(i)
    return e_resultado