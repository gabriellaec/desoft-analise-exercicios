def quantos_uns(numero):
    n = str(numero)
    contador = 0
    for x in n:
        if x == '1':
            contador += 1
    return contador