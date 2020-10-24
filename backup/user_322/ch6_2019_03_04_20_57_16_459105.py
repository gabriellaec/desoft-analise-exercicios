def encontra_maximo(matriz):
    a = max(matriz[0])
    b = max(matriz[1])
    c = max(matriz[2])
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c