def raiz_quadrada(numero):
    i=1
    while i<numero:
        numero-=i
        i+=2
    return numero