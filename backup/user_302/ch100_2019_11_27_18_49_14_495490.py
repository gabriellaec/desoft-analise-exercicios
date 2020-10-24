lista_logins = []
login = input("Digite um login: ")
if login != "fim":
    if login in lista_logins:
        login = login_disponível(login, lista_logins)
        lista_logins.append(login)
    else:
        lista_logins.append(login)
else:
    print(lista_logins)