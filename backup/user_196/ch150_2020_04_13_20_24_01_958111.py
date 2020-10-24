import math
def calcula_pi(n):
    valordepi = 0
    for i in range (1,n+1):
        valordepi += (6/(i**2))
        k = math.sqrt(valordepi)
        print(k)
    return k
