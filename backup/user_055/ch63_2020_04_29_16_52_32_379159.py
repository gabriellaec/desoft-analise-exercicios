def pos_arroba(e_mail):
    posicao_arroba = e_mail.find('@')
    return posicao_arroba

def nome_usuario(e_mail):
    x = pos_arroba(e_mail)
    nome = e_mail[0:x]
    return nome