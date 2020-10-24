import math
def calcula_pi(n):
    i = 1
    soma = 0
    while i < n:
        pi = 6/i**2
        soma = soma + pi
        i+=1
    print (math.sqrt(soma))
    return math.sqrt(soma)