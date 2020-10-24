from math import factorial
def calcula_euler(x,n):
    lista = []
    i = 0
    while i < n:
        f = factorial(i)
        lista.append((x**i)/f)
        i += 1
    return sum(lista)