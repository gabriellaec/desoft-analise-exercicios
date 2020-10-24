
login = input('Qual seu login?')
while login != 'fim':
    lista_logins = []
    login_available = login_disponivel(login,lista_logins)
    print(login_available)
    if login == login_available:
        lista_logins.append(login)
    else:
        login = input('Qual seu login?')