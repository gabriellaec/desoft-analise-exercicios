def quantos_uns(numero):
    numero = str(numero)
    uns = 0
    for i in numero:
        if i == '1':
            uns += 1
    return uns