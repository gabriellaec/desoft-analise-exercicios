def login_disponivel(login, lista_logins):

    login_retornado=login
    incrementador = 1;
    for login_cadastrado in lista_logins:
        #verifica se a string contem o login
        if login in login_cadastrado:
            #pega o numero apos o login
            valor_login = login_cadastrado.replace()

            if(valor_login != "):
                incrementador = incrementador + int(valor_login)
                login_retornado = login + str(incrementador)
            else:
                login_retornado = login + "1"

    return login_retornado


input_texto = ""
lista_logins = []

while(input_texto != "fim"):
    input_texto = input("Digite um login: ")

    if(input_texto != "fim"):
        login_atualizado =  login_disponivel(input_texto, lista_logins) 
        print(login_atualizado)
        lista_logins.append(login_atualizado)