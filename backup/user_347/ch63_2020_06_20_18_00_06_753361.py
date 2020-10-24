def nome_usuario(email):
    i = 0
    while i<len(email):
        if email[i] == '@':
            nome = email - email[::-i]
        else:
            i += 1
    return nome