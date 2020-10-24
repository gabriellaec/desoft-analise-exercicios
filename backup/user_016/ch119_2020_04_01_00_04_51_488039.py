from math import factorial
def calcula_euler(x,n):
    lista = []
    i = 0
    f = factorial(i)
    while i < n:
        lista.append((x**i)/f)
        i += 1
    return lista
    
    