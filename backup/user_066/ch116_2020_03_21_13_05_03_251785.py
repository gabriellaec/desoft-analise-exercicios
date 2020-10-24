def raiz_quadrada(x):
    i = 1
    raiz = 0
    while x!=0:
        x -= i
        i += 2
        raiz += 1
    return raiz