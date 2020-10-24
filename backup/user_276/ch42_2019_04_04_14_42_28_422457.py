def quantos_uns(numero):
    i = 0
    s = 0
    numero = str(numero)
    while i < len(numero):
        if numero[i] == '1':
            s += 1
        i += 1
    return s

