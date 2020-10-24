def nome_usuario(email):
    ar = email.find('@')
    return email[0: ar]