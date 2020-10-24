def raiz_quadrada(quadrado):
    x = quadrado
    i = 0
    raiz = 0
    while x > 0:
        x = x - (2*i + 1)
        raiz += 2*i + 1
        i += 1
    return raiz

print(raiz_quadrada(225))