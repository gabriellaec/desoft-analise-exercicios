def quantos_uns(x):
    contador = 0
    for i in str(x):
        if i == '1':
            contador += 1
    return contador