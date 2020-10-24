def nome_usuario(e_mail):
    
    arroba = e_mail.index('@')
    return e_mail[:arroba]