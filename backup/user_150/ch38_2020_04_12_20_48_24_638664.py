def quantos_uns(numero):
    contador = 0
    numero = str(numero)
    for um in numero:
        if um == '1':
            contador += 1
    return contador