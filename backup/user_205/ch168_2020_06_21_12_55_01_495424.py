def login_disponivel(login, lista):
    contador = 0 
    if login not in lista:
        return login 
    else:
        while(login in lista):
            contador +=1 
            novo_login = login + str(contador)
            if novo_login not in lista:
                return novo_login
            else:
                contador += 1
                novo_login = novo_login.replace(novo_login[-1],str(contador))
                if novo_login not in lista:
                    return novo_login
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
                if login_novo not in lista:
                    return login_novo
                else:
                    numero += 1
                    novo_login = login_novo.replace(login_novo[-1], str(numero))
                    return novo_login
                #ATENÇÃO!!!!! Código errado que da certo
                
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
                if login_novo not in lista:
                    return login_novo
                else:
                    while(login_novo in lista):
                        numero+=1
                        novo_login = login_novo.replace(login_novo[-1], str(numero))
                        if novo_login not in lista:
                            return novo_login 