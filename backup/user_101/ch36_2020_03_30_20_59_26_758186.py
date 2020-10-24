def fatorial(n):
    contador = n - 1
    fat = n
    while contador > 1:
        fat *= contador
        contador -= 1
    return fat

