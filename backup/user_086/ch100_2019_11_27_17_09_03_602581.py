lista_logins = []
login = 0
while login!='fim':
    login = input('Digite um nome de usuário: ')
    if not login =='fim':
        login_disp = login_disponivel(login,lista_logins)
        lista_logins.append(login_disp)
        print(login_disp)
    else:
        for l in lista_logins:
            print(l)