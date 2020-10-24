def raiz_quadrada(numero):
    i = 1
    x = numero 
    contador = 0
    while x > 0:
        x = x - i
        i+=2
        contador += 1
    return contador
        