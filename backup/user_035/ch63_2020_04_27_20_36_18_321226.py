def nome_usuario(email):
    x = email.find('@')
    nome = email[0]
    e = 1
    while e < x:
        email[e].join(nome)
        e += 1
    return nome