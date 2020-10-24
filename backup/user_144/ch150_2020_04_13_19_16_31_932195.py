from math import sqrt
def calcula_pi(n):
    soma = 0
    i = 0
    indice = 1
    while i < n:
        soma +=6/(indice**2)
        i+=1
        indice+=1
    return sqrt(soma)