def nome_usuario(email):
    nome = ''
    for i in email:
        if i != '@':
            nome = nome+i
        else:
            return nome