import math

def calcula_pi(n):
    soma = 0 
    for e in range(1,(n + 1)):
        num = (6)/(e**2)
        soma += num
    pi = math.sqrt(soma)
    return pi