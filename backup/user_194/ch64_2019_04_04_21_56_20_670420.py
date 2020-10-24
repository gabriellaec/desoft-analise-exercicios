def nome_usuario(string):
    usuario = ''
    email = str(string)
    i = 0
    while i < len(email):
        if email[i] == '@':
            usuario = email[0,i]
        i += 1
    return usuario
       
        