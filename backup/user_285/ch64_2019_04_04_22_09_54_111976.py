def nome_usuario(email):
    posicao=pos_arroba(email)
    nome=email[0,posicao]
    return nome