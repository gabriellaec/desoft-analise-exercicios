import math
def calcula_pi (n):
    numero = 0
    contador = 1
    while contador<= n:
        numero = numero + (6/contador**2)
        contador = contador + 1
    pi = math.sqrt(numero)
    return pi