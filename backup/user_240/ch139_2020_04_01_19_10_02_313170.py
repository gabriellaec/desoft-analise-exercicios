def arcotangente(x, n):
    resultado = 0
    for i in range(n):
        resultado += (x ** (2 * i))/(2 * i) * (-1 ** (i))
    return resultado
        