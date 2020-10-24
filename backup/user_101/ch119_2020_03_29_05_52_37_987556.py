import math

def calcula_euler(x, n):
    contador = 0
    ex = 0
    while n >= contador:
        ex += (x ** contador)/(math.factorial(contador))
        contador += 1
    return ex