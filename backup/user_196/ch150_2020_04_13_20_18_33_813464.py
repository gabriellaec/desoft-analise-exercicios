import math
def calcula_pi(n):
    valordepi = 0
    for i in range (1,n+1):
        k = math.sqrt(6/(i**2))
        valordepi += k
        print(valordepi)
    return valordepi
