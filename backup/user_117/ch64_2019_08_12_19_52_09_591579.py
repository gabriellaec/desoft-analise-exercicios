def nome_usuario(email):
    i=0
    while i<len(email):
        if email[i]=='@':
            del email[i]
    return email
    
    