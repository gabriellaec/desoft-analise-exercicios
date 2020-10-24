logins_salvos =['andre', 'fabio', 'lucio', 'lucio1']

inserir_login = 0

while inserir_login != 'fim':
    inserir_login = input("Digite seu login: ")

    disponivel = login_disponivel(inserir_login, logins_salvos)
    logins_salvos.append(disponivel)

    for login in logins_salvos:
        print (login, "\n")