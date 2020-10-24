def quantos_uns(numero):
    i = 0
    contador = 0
    while i < len(numero):
        if numero[i] == 1:
            contador = contador + 1
        i += 1
    return contador