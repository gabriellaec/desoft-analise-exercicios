def nome_usuario(x):
    i = 0
    while i < len(x):
        if x[i] < '@':
            return x[:i]
        i+=1