import math
def calcula_pi (n):
    numero = 1
    for contador in range(n):
        numero = numero + (6/contador**2)
    pi = math.sqrt(numero)
    return pi