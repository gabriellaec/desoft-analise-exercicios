def login_disponivel (login, lista_login):
    # chega se o login está na lista. Se não estiver, retorna o login disponivel
    if login not in lista_login:
        return login
    
    # se estiver:
    else:
        i = 1
        pesquisa = True
        while pesquisa:
            if login + str(i) not in lista_login: # se não estiver na lista
                pesquisa = False
                return login + str(i)
            else: # se estiver, aumenta o índice e analisa de novo
                i += 1
        