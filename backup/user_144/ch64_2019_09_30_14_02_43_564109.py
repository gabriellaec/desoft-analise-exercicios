def extrai_usuario(email):
    pos = pos_arroba(email)
    return email[:pos]