def login_disponivel(login, lista):
    print(login)
    print(lista)
    for logins in lista:
        if login not in lista:
            print('oi')
            return login
        else:
            print (lista[-1][-1])
            if int(lista[-1][-1]) > 0:
                numero = int(lista[-1][-1]) + 1
                login = login + str(numero)
                return login 
            else:
                numero = '1'
                login = login + numero
                return login 