import math
def calcula_euler(x,n):
    contador=1
    resultado=0
    while contador<n:
        if n<=2:
            resultado+=x
            contador+=3
        else:
            resultado+=(x**contador/math.factorial(contador))
            contador+=1
    resultado+=1
    return resultado
