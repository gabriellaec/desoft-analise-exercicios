def quantos_uns(numero):
    n = 0
    i = 0
    for i in numero:
        if numero[i] == 1:
            n += 1
        else:
            i += 1
    return n