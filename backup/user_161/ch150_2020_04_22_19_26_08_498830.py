import math
def calcula_pi(n):
    soma = 0
    for i in range(n):
        soma += 6 / (n+1)**2
    return math.sqrt(soma)