def nome_usuario(email):
    for i in range(len(email)):
        if email[i]=='@':
            return email[:i]