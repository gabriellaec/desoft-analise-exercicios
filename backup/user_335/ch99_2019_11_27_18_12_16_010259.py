def login_disponivel (login_user,login_disponivel):
    novologin = login_user

    for login in login_disponivel:

        if login == login_user:
            contador = 0
            for l in login_disponivel:
                if l[:(len(login))] == login:
                    contador += 1

            n = str(contador)
            novologin = login+n
    
    return novologin