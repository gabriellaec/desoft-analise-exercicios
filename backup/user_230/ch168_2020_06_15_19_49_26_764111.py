def login_disponivel(login, lista):
    novo_login=0
    num=0
    if login not in lista:
        lista.append(login)
        return login
    else:
        for logins in lista:
            if login!=logins:
                continue
            else:
                num+=1
                novo_login=login+str(num)
                if novo_login not in lista:
                    return novo_login
                else:
                    while novo_login in lista:
                        num+=1
                        outro_login=novo_login.replace(novo_login[-1], str(num))
                        if outro_login not in lista:
                            return outro_login