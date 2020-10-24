def login_disponivel (login_usuario, logins):
    c = 0
    for login in logins:
        if login_usuario in login:
            c += 1
    if c == 0:
        return login_usuario
    else:
        string =  str(c + 1) 
        login_usuario += string
        return login_usuario 
    