import math
def calcula_euler(x,n):
    contador=0
    x=0
    while(x<n):
        x+=x**contador/math.factorial(contador)
    contador+=1
    return x