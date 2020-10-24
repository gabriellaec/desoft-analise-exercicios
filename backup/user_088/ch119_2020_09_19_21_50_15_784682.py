import math
def calcula_euler(x,n):
    contador=2
    inicio=1+x
    while(contador<n):
        inicio+=x**contador/math.factorial(contador)
        contador+=1
    return inicio