def impares(x):
    impar = 2*x + 1
    return impar

def raiz_quadrada(n):
    i = 0
    while n > 0:
        n = n - impares(i)
        i += 1
        return i