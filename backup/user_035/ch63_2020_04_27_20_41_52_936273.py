def nome_usuario(email):
    x = email.find('@')
    nome = email[0]
    for e in range(x):
        email[e].join(nome())
    return nome