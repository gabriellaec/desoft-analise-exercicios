import math
def calcula_pi(n):
    lista = []
    for elemento in range(1, n+1):
        lista.append(6/(elemento**2))
    return math.sqrt(sum(lista))