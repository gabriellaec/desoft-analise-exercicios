def nome_usuario(email):
    nome = email.find('@')
    return email[0:nome:1]