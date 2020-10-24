import math
def calcula_pi(n):
    soma=0
    i=1
    while i<=len(n):
        pi=(6/i**2)
        soma=soma+pi
    return math.sqrt(soma)