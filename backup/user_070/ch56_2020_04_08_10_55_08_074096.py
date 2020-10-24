def calcula_norma(lista):
    x = 0
    for i in lista:
        x += i**2
    x = x**0.5
    return x