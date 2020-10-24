#expoente = a
#divisor = b


from math import *

def arcotangente (x,n):
    positivo = 0
    negativo = 0
    b = 3
    a = 3
    i = 1
    
    while i < n:
        if i%2 == 0:
            positivo += + x**a/b
        elif  i%2 == 1:
            negativo += x**a+2/b+2
        b += 2
        a += 2
        i += 1
        
    y = (pi/180)*(x + positivo - negativo)
    return y
    