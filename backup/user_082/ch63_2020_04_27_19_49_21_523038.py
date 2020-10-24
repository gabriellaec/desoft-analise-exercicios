def nome_usuario(email):
    pos_arroba= email.find('@')
    return email[:pos_arroba]