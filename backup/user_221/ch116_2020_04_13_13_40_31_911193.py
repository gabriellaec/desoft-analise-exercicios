def raiz_quadrada(n):
    m = 1
    contador = 0
    while m <= n:
        if n == 0:
            contador = 0
        elif n == 1:
            contador = 1
        else:        
            n = n - m
            contador += 1
        m += 2
    return contador