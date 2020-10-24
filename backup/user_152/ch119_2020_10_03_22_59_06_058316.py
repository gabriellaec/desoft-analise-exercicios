import math
def calcula_euler (x, n):
    contador = 0
    resultado = 0
    while contador<n:
        resultado +=(x**i)/math.factorial(i)   
        contador += 1
    return resultado