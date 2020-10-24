import math
def calcula_euler (x,n):
    i = 0
    lista = []
    t = []
    e = 1
    while i <= n:
        t[i] = x**i/math.factorial(i)
        lista.append(t[i])
    e = 1 + sum(lista)
    return e
        
    