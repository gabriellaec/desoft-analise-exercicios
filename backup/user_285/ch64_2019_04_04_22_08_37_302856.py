def nome_usuario(email):
    posicao=pos_arroba(email)
    return email[:posicao]