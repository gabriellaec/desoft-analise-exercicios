import math
def calcula_pi(n):
    valordepi = 0
    soma = 0
    for i in range (1,n+1):
        soma += (6/(i**2))
        valordepi = math.sqrt(soma)
        print(valordepi)
    return valordepi
