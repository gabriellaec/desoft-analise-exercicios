def login_disponivel(login, listalog):
    i = 1
    for i in range (len(listalog)):
        if login not in listalog:
            return login
        else:
            for i in range (len(listalog)):
                while login in listalog:
                    login += str(i)
                if login in listalog:
                    login = login[:-1]
                i+=1
            return login