import string
def login_disponivel(login, lista):
    numero = 0
    #Se o login não está na lista, devolve sem alteração! 
    if login not in lista:
        return login
    #Login está na lista! 
    else:
        for logins in lista: 
            #Se o login for diferente, continua o loop
            if login != logins:
                continue
            #Login igual!
            else:
                numero +=1
                login_novo = login + str(numero)
                print (login_novo)
                if login_novo not in lista:
                    return login_novo
                else:
                    print(numero)
                    numero += 1
                    print(numero)
                    novo_login = login_novo.replace(login_novo[-1], str(numero))
                    print(novo_login)
                    return novo_login