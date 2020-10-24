def login_disponivel(login, indisponivel):
    if login not in indisponivel:
        return login
    else:
        qtd = 0
        for utilizado in indisponivel:
            if utilizado[:len(login)] == login:
                qtd += 1
        return login + '{}'.format(qtd)