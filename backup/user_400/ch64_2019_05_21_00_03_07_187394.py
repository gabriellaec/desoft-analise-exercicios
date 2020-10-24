def nome_usuario(x):
    posi = 0
    for i in range(len(x)):
        if x[i] == '@':
            posi = i
    return x[0:posi]