def nome_usuario (email):
    localizacao = email.find('@')
    return email[:localizacao]