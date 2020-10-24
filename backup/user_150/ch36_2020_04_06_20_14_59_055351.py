def fatorial(n):
    numero = 1
    multiplicacao = 1
    while numero <= n:
        multiplicacao *= numero
        numero += 1
    return multiplicacao