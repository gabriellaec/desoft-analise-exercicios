def login_disponivel(login, listalog):
    for i in range (len(listalog)):
        if login not in listalog:
            return True
        else:
            for i in range (len(listalog)):
                loginfinal = login + i
    return loginfinal