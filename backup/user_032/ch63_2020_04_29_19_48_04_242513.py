def nome_usuario(email):
    e = email.find('@')
    return email[:e]