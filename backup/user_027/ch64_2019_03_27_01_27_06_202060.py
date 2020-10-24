def nome_usuario(x):
    for i in range(len(x)):
        if x[i] == '@':
            pos_arroba = i
            break
    return x[:pos_arroba]