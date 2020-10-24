def fatorial(n):
    i = n - 1
    resultado = n
    while i > 0:
        resultado = resultado * i
        i -= 1
    return resultado
