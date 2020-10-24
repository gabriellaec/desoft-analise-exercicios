def raiz_quadrada(n):
    s = 1
    m = n
    contador = 0
    while m >= s:
        m = m - s
        s += 2
        contador += 1
    return contador