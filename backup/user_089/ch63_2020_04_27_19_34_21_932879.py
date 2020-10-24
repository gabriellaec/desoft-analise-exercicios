def nome_usuario(x):
    i = 0
    while i < len(x):
        if x[i] == '@':
            numero = i
            return x[:numero]
        else:
            i += 1