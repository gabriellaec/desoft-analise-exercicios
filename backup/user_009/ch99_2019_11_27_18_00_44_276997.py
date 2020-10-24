def login_disponivel(login, l_exist):
    if login not in l_exist:
        l_exist.append(login)
        return login
    else:
        for i in range(1,1000):
            if login != login + str(i) and login + str(i) not in l_exist:
                login = login + str(i)
                l_exist.append(login)
                break
        return login