import math as mt
def calcula_pi(n):
    soma = 0
    for i in range(n):
        soma += mt.sqrt(6/(n**2))
        print (soma)
    return soma