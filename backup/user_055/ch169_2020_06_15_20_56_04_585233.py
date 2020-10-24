def login_disponivel(login, indisponivel):
    if login not in indisponivel:
        return login
    else:
        qtd = 0
        for utilizado in indisponivel:
            if utilizado[:len(login)] == login:
                qtd += 1
        disponivel = login + '{}'.format(qtd)
        return disponivel

lista_logins = []
login = ''
while login != 'fim':
    login = input('Digite seu login: ')
    disponivel = login_disponivel(login, lista_logins)
    if disponivel != 'fim':
        lista_logins.append(disponivel)
for logins in lista_logins:
    print(logins, lista_logins)