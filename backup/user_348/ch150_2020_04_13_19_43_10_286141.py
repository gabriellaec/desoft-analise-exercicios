import math
def calcula_pi (n):
    numero = 0
    for contador in range(1,n):
        numero = numero + (6/contador**2)
    pi = math.sqrt(numero)
    return pi