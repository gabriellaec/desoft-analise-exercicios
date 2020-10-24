def raiz_quadrada(numero):
    n = int(numero)
    n_vezes = 0
    impar = 1
    while numero != 0:
        numero = numero - impar
        impar += 2
        n_vezes += 1
    return n_vezes