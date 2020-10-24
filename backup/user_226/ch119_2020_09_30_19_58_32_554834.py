import math

def calcula_euler(x, n):
    lista = []
    i = 0
    while i < n:
        lista.append(x ** i/ math.factorial(i))
        i += 1
    return sum(lista)