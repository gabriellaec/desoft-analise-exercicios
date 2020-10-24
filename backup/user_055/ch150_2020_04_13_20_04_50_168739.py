from math import sqrt
def calcula_pi(n):
    i = 1
    lista_pi = []
    while len(lista_pi) < n:
        pi = (6/(i**2))
        lista_pi.append(pi)
        i += 1
    return sqrt(sum(lista_pi))