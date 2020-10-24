def fatorial (n):
    fat = 1
    contador = 2
    while n+1 > contador:
        fat *= contador
        contador += 1
    return fat

