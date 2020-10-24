def login_disponivel(proposta_login, lista_logins):

    contador = 1

    for logins in lista_logins:

        if len(logins)>5:

            login_sem_numero = logins[:-1]

            if login_sem_numero == proposta_login:

                contador = contador + 1

                return proposta_login + str(contador)

        else:

            return proposta_login + str(contador)

    else:

        return proposta_login