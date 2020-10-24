import math as m
def calcula_pi(n):
    cont = 1
    soma = 0
    while cont<n:
        soma += 6/(cont**2)
        cont += 1
    pi = m.sqrt(soma)
    return pi
