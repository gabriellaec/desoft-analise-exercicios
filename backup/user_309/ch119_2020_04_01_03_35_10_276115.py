import math
def calcula_euler(x,n):
    resultado = 0
    i = 1
    while i < n:
        if n <= 2:
            resultado += x
            i += 3
        else:
            resultado += (x**i/math.factorial(i))
            i += 1
        resultado = resultado + 1
        return resultado 
            