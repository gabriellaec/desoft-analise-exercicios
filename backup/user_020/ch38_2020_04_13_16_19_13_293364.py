def quantos_uns(numero):
    i = 0
    n = 0
    while i < len(numero):
        if numero[i] == 1:
            n += 1
        else:
            i += 1
    return n