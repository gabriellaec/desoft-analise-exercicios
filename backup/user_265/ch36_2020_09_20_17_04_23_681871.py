def fatorial(n):
    resultado = n*(n-1)*(n-2)*...*1
    i = 1
    while i <= n:
        resultado *= i
        i += resultado
    return resultado
