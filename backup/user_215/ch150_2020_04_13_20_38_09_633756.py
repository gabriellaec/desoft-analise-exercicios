def calcula_pi(n):
    i = 1
    valor = 0
    while i != n:
        valor += (6/(i**2))
        valor = valor ** 0.5
        i += 1
    return valor