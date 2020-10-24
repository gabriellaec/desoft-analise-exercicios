import math
def calcula_pi(n):
    soma=0
    for i in range(1,n):
        pi=(6/i**2)
        soma=soma+pi
    return math.sqrt(soma)