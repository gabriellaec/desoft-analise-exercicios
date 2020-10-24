def nome_usuario(x):
    nome = ''
    i = 0
    for e in x:
        if e != '@':
            nome += e
    return nome  