def quantos_uns(numero):
    n = str(numero)
    qntd_uns = 0
    for i in range (0,len(n)):
        if n[i] == '1':
            qntd_uns += 1
    return qntd_uns