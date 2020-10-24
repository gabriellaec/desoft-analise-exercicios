def pos_arroba(email):
    posicao=0
    arroba=0
    for e in email:
        if e=='@':
            arroba=posicao
        posicao+=1
    return arroba

def nome_usuario(email):
    arroba=pos_arroba(email)
    return email[:arroba]