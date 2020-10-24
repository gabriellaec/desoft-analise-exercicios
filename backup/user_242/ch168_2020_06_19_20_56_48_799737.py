def login_disponivel(login, indisponivel):
    if login nnot in indisponivel:
        return login
    
    else:
        quantidade = 0
        for utilizado in indisponivel:
            if utilizado[:len(login)] == login:
                quantidade+=1
        return login + '{}'.format(quantidade)