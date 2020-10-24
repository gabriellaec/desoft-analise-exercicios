
import math
import sys
sys.float_info.dig

def arcotangente(x,n):
    resultado = 0
    contador = 1

    while contador != n:
        numerador = x**contador

        divisão = (numerador/contador)
        #format(float(divisão), '6g')
        

        resultado = resultado +(x -  divisão)

        contador = contador + 2

    conversor = math.radians(resultado)

    return resultado