import math
def calcula_pi(n):
    soma=0
    i=1
    while i<=n:
        pi=(6/i**2)
        soma=soma+pi
        i+=1
    return math.sqrt(soma)