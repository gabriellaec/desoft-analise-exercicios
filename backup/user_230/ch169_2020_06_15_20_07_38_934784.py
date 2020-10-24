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
                    lista.append(novo_login)
                    return novo_login
                else:
                    while novo_login in lista:
                        num+=1
                        outro_login=novo_login.replace(novo_login[-1], str(num))
                        if outro_login not in lista:
                            lista.append(outro_login)
                            return outro_login
lista=[]
login=input("Escolha logins(um por vez) e quando acabar digite fim:")
while login!="fim":
    disponivel=login_disponivel(login, lista)
    lista.append(disponivel)
    print("{0}".format(disponivel))
    login=input("Escolha logins(um por vez) e quando acabar digite fim:")
