def login_disponivel (login_usuario, logins):
    c = 0
    for login in logins:
        if login_usuario in login:
            if login == login_usuario:
                c += 1
            else:
                m = len(login) - len(login_usuario)
                indice = (len(login_usuario) - 1) + m
                d = login[indice] 
                v = d.isdigit()
                if v == True:
                    c += 1
    if c == 0:
        return login_usuario
    else:
        string = str(c) 
        login_usuario += string
        return login_usuario 
    