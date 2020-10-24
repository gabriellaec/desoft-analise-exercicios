def login_disponivel(login, lista_logins):
    if login in lista_logins:
        for i in range(len(lista_logins)):
            if '{0}{1}'.format(login, i) not in lista_logins:
                return '{0}{1}'.format(login, i)
    else:
        return login