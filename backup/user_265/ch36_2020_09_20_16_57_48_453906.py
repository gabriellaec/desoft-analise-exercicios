def fatorial(n):
    resultado = 1
    i = 1
    while i <= n:
        resultado *= i
        i += resultado
    return resultado