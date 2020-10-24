lista_logins = []
login = input("Insira um login: ")
while login != 'fim':
    if len(lista_logins) != 0:
        lista_logins.append(login_disponivel(login,lista_logins))
    else:
        lista_logins.append(login)
    login = input("Insira um login: ")
print(lista_logins)