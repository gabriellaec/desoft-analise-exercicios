def nome_usuario(email):
    x = -1
    i = 0
    while i<len(email):
        if email[i] == '@':
            x = i
    return (email[:x])
            