def login_disponivel(login,lista_existentes):
    not_done = True

    if login not in lista_existentes:
        return login

    else:  
        contador = 1
        while not_done:
            if login+str(contador) not in lista_existentes:
                not_done = False

            else:
                contador += 1
        return login+str(contador)
