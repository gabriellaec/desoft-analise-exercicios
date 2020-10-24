def nome_usuario(email):
    s = email.find('@')
    return email[ :s]
    