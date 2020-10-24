def nome_usuario(email):
    x = str(email)
    i = 0
    while i<len(x):
        if x[i]=='@':
            return x[:i]
        i += 1