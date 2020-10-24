def raiz_quadrada(n):
    i = 1
    contador=1
    while i<n:
        n = n - i
        i+=2
        contador+=1
    return contador