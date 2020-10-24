def login_disponivel(login, lista_logins):

    login_retornado=login
    incrementador = 1;
    for login_cadastrado in lista_logins:
        #verifica se a string contem o login
        if login in login_cadastrado:
            #pega o numero apos o login
            valor_login = login_cadastrado.replace(login, "")

            if(valor_login != ""):
                incrementador = incrementador + int(valor_login)
                login_retornado = login + str(incrementador)
            else:
                login_retornado = login + "1"
                
    return login_retornado



print(login_disponivel('lucio', ['andre', 'fabio']))
print(login_disponivel('lucio', ['andre', 'fabio', 'lucio']))
print(login_disponivel('lucio', ['andre', 'fabio', 'lucio', 'lucio1']))