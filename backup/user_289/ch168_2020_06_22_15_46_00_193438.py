def login_disponivel(novo_login, lista_logins):
    if novo_login not in lista_logins:
        return novo_login
    else:
        i = 1
        for logins in lista_logins:
            while novo_login in lista_logins:
                novo_login += str(i)
                if novo_login in lista_logins:
                    novo_login = login[:-1]
                i += 1
            return novo_login