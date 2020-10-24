def soma(x):
    while x < 100:
        resultado = 1/(2 ** (x - 1)) + 1/(2 ** x)
        x += 1
    return resultado

i = 1
print(soma(i))