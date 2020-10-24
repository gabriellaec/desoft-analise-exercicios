def pos_arroba(e_mail):
    posicao_arroba = e_mail.find('@')
    return posicao_arroba

def pos_ponto(e_mail):
    posicao_ponto = e_mail.find('.')
    return posicao_ponto

def nome_usuario(e_mail):
    x = pos_arroba(e_mail)
    y = pos_ponto(e_mail)
    nome_1 = e_mail[0:y]
    nome_2 = e_mail[(y+1):x]
    nome_completo = ' '.join([nome_1, nome_2])
    return nome_completo