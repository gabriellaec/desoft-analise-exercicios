import math
def calcula_euler(x,n):
    contador=0
    soma=0
    while(contador<n):
        soma+=x**contador/math.factorial(contador)
        contador+=1
    return soma