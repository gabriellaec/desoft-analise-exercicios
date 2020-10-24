
import math
def arcotangente(x,n):
    resultado = 0
    contador = 3

    while contador != n:
       

        resultado += x - x**contador/contador

        contador = contador + 2

   

    return resultado