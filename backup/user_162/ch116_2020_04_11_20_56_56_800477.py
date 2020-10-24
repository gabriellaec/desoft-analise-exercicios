def raiz_quadrada(n):
    impares = 1
    i = 0
    while n >= 0:
        n -= impares
        i+=1
        impares+=2
    return i 