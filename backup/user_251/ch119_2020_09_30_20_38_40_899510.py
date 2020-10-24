import math
def calcula_euler(x, n):
    expoente = 0
    resultado = 0
    while expoente < n:
        resultado += (x**expoente)/(math.factorial(expoente))
        expoente += 1
        
    return resultado
    
    