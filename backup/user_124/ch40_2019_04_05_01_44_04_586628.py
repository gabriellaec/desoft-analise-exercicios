def fatorial (n):
    contador = 1
    while contador <  n:
        x = (n + contador) * (n + (contador + 1))  
        contador += 1
        return x

    