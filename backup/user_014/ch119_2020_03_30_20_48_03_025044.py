def fatorial (n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def calcular_euler(x,n):
    i = 1
    contador = 1
    while i < n:
        contador = contador + (x**i)/ fatorial(i)
        i += 1
    return contador
    