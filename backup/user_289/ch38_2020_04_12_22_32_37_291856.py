def quantos_uns(numero):
    qntd_uns = 0
    i = 0
    while i < len(numero):
        if numero[i] == 1:
            qntd_uns += 1
        i += 1
    return qntd_uns