def login_disponivel (login, lista):
    if login not in lista:
        return login
    else:
        soma = 0
        for i in lista:
            if i[:len(login)] == login:
                soma += 1
        disponível = login + "{}" .format(soma)
        return disponível

lista_nova = []
login = ""
while login != "fim"
    login = input("Digite seu login: ")
    disponível = login_disponivel(login, lista_nova)
    if disponível != "fim":
        lista_nova.append(disponível)
for logins in lista_nova:
    print (logins, lista_nova)