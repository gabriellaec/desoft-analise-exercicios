import math
def calcula_pi(n):
    i=0
    soma=0
    while i<=n:
        soma=soma+6/i**2
        i=i+1
    pi=math.sqrt(soma)
    return pi