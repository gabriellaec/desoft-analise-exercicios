def login_disponivel(login, indisponivel):
    c = 0
    for i in indisponivel:
        if i in login:
            c+=1
        if c == 0:
            return login
        else:
            return login+c