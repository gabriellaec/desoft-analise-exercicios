def fatorial(n):
    contador = n
    fat = n
    while contador > 1:
        fat *= (fat-1)
        fat -= 1
        contador -= 1
    return fat

