def raiz_quadrada(quadrado):
    x = quadrado
    i = 0
    while x > 0:
        x = x - (2*i + 1)
        i += 1
    return i

print(raiz_quadrada(225))