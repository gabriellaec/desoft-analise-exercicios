from math import factorial

def calcula_euler(x, n):
    lista_euler = []
    for e in range(n):
        lista_euler.append((x**e)/factorial(e))
    return (sum(lista_euler))