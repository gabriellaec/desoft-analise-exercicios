def nome_usuario (email):
    pos = email.find('@')
    nome = email[:pos]
    return nome

