def nome_usuario(email):
    x = email.find('@')
    return email[:x]