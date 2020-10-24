import math
def calcula_pi(n):
    soma=0
    for i in range(n):
        pi=(6/i**2)
        soma=soma+pi
    return math.sqrt(soma)