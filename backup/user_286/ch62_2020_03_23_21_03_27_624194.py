def pos_arroba(e_mail):
    for caracter in e_mail:
        if caracter == '@':
            posicao = e_mail.index(caracter)
            return posicao