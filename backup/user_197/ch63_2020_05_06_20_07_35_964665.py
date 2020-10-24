def nome_usuario(email):
    x = -1
    i = 0
    while i<len(email):
        if email[i] == '@':
            x = i
        i += 1
    return (email[:x])
            