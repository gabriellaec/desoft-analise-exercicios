def login_disponivel(login, lista_logins):
    i = 1
    if login not in lista_logins:
        return login
    else:
        return lista_login[login] + "i"

login = input("Digite um login: ")
while login != 'fim':
    print(login)
    login = input("Digite um login: ")
    print(login)
    
