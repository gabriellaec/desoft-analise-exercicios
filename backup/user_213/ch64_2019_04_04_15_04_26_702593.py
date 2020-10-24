def pos_arroba(email):
    posicao=0
    i=0
    while email[i]!='@':
        posicao+=1
        i+=1
    return posicao
def nome_usuario(email):
    posicao=pos_arroba(email)
    nome=email[:posicao]
    return nome
