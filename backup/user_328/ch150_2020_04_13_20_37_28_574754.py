import math
def calcula_pi(n):
    cont = 1
    soma= 0
    while cont <= n: 
        soma += (6/(i**2))
        cont += 1
    pii = math.sqrt(soma)
    return pii