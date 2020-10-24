def raiz_quadrada(n):
    ímpar = 1
    i = 0 
    while not n <= 0:
        n = n - ímpar
        ímpar += 2
        i += 1
    return i