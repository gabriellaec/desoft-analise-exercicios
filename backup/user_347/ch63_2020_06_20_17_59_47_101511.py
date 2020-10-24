def nome_usuario(email):
    i = 0
    while i<len(email):
        if email[i] == '@':
            nome = email - email[::-i]
    return nome