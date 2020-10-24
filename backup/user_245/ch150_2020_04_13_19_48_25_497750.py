import math as mt
def calcula_pi(n):
    soma = 0
    for i in range(n):
        soma +=6/(n**2)
    sqrt = mt.sqrt(soma)
    return sqrt