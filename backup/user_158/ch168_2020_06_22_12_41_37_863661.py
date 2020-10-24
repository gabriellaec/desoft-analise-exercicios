def login_disponivel(login,usuarios):
    if login not in usuarios:
        return login
    else:
        i = 0 
        for utilizado in indisponivel:
            if utilizado[:len(login)]==login:
                i += 1
        return +"{}".format(i)