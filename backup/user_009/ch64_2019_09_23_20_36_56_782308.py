def nome_usuario(x):
    for i in range(len(x)):
        if x[i] == '@':
            a = i
    nome = x[:a]
    return nome