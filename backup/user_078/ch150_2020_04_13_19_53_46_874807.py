import math
def calcula_pi(n):
    i=0
    calculo = True
    soma = 0
    while calculo:
        if i<=n:
            soma += math.sqrt(6/i**2)
            i+=1
        else:
            calculo = False
    return soma