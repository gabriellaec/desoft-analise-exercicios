import math
def calcula_pi(n):
    valordepi = 0
    for i in range (1,n+1):
        valordepi += math.sqrt(6/n**2)
        print(valordepi)
    return valordepi
