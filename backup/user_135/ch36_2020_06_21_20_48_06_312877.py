def fatorial(n):
    contador = n
    fatorial = n
    while contador > 1:
        fatorial *= contador-1
        contador -= 1
    return fatorial