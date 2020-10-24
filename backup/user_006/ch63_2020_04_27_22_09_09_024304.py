def nome_usuario(email):
    arroba=pos_arroba(email)
    usuario=email[:arroba]
    return usuario