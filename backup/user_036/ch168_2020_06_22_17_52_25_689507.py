def login_disponivel(login, indisponivel):
    c = 0
    if login in indisponivel:
        for i in indisponivel:
            if login in i:
                c+=1
    if c == 0:
        return login
    else:
        return login+str(c)

