import math
def arcotangente(x,n):

    arctan = 0
    contador = 1
    contador2 = 0

    while contador2 < n:
        arctan = arctan + x - ((x**contador)/contador)
        contador = contador + 2
        contador2 = contador2 + 1

    
    return arctan