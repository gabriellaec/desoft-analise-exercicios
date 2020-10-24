def nome_usuario(email):
    nome = ' '
    i = 0
    while i < len(email):
        if email[i] == '@':
            nome = email[:i]
        i += 1
    return nome

            
            