def quantos_uns(numero):
    contador = 0
    for n in numero:
        if n == 1:
            contador += 1
        else:
            contador = 0
    return contador