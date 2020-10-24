def nome_usuario(email):
    posicao=pos_arroba(email)
    nome=email[:posicao-1]
    return nome
