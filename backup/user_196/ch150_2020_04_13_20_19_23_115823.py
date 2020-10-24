import math
def calcula_pi(n):
    for i in range (1,n+1):
        valordepi += math.sqrt(6/(i**2))
        print(valordepi)
    return valordepi
