import math 

i=1
n=0
def calcula_euler (x,n):
    while ( n < i):
        if n <= 2 :
            resultado = i + x
            i += 3 
        else:
            resultado = 1 + x + ((x**i) / math.factorial (i))
            i += 1
    return resultado