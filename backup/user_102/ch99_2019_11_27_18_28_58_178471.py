def login_disponivel(logins):
    login = input("login:")
    numero = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    d = 0
    for i in logins:
        if login != i:
            logins.append(login)
            return login
        else:
            loginnovo = login+numero[d]
            logins.append(loginnovo)
            return(loginnovo)
            d += 1