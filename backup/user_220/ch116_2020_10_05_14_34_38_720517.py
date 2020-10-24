def raiz_quadrada(numero):
    i = 1
    x = numero - i
    contador = 1
    while x != 0:
        i+=2
        x = x - i
        contador += 1
    return contador
        