def fatorial(n):

    resultado = 1

    if n == 0:
        return resultado
    else:
        while n > 0:
            resultado = resultado * n
            n -= 1

        return resultado

print(fatorial(4))