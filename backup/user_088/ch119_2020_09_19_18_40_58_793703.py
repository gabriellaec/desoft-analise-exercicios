import math
def calcula_euler(x,n):
    contador=0
    soma=0
    while(soma<n):
        nova_soma=soma+=x**contador/math.factorial(contador)
    contador+=1
    soma+=1
    return nova_soma