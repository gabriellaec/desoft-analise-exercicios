def login_disponivel(login, listalogin):
    i = 1
    if login not in listalogin:
        listalogin.append(login)
    else:
        login = login + str(i)
        i += 1
    return login

while login not in listalogin:
    if login != "fim"
        listalogin.append(login)
        login = input("Digite o login desejado: ")
    else:
        print(listalogin)
    