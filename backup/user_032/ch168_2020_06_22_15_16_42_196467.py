def login_disponivel(login,logins_existentes):
    if login not in logins_existentes:
        return login
    else:
        quantidade = 0
        for utilizado in logins_existentes:
            if utilizado[:len(login)] == login:
                quantidade += 1
        return login + '{0}'.format(quantidade)