def login_disponivel(login, lista_logins):
    if login in lista_logins:
        for i in range(len(lista_logins)):
            if login+i not in lista_logins:
                return login+i
    else:
        return login