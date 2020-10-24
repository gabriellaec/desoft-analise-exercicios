def nome_usuario(email):
    pos=pos_arroba(email)
    return email[:pos]