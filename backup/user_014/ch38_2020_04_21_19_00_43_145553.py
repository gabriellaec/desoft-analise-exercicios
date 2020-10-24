def quantos_uns(numero):
    n = 0
    contador = 0
    while n < len(numero):
        if numero[n] == '1':
            contador += 1
        else:
            contador += 0
        n += 1
    return contador           