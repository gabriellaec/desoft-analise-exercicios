from math import *
def calcula_tempo (n):
    soma = 0
    i = 1
    while i - 1 < n:
        soma += 6/(i**2)
        i = i + 1  
    pi = soma**0.5
    return pi