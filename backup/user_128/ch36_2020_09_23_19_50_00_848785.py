def fatorial(n):

    resultado = 1

    while n > 0:
        resultado = resultado * n
        n -= 1

    return resultado

print(fatorial(4))