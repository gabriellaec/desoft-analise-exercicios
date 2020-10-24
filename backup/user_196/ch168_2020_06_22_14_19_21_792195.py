def login_disponivel(login, listalog):
    c = 1
    for i in range (len(listalog)):
        if login not in listalog:
            return login
        else:
            for i in range (len(listalog)):
                while login in listalog:
                    login += str(c)
                if login in listalog:
                    login = login[:-1]
                c+=1
            return login