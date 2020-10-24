def login_disponivel(login_disponivel):
    list_login = []
    i = 0
    for e in login_disponivel:
        if not e in login_disponivel:
            list_login.append(e)
        else:
            list_login.append(e+i)
    return list_login