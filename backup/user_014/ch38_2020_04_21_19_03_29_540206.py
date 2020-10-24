def quantos_uns(numero_qualquer):
    n = 0
    contador = 0
    while n < len(numero_qualquer):
        if numero_qualquer[n] == '1':
            contador += 1
        else:
            contador += 0
        n += 1
    return contador