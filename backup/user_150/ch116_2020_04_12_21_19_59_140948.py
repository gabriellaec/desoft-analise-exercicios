def raiz_quadrada(numero):
    i = 1
    contador = 0
    while i <= numero:
        numero -= i
        i += 2
        contador += 1
    return contador