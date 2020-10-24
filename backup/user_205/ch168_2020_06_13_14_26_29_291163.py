import string
def login_disponivel(login, lista):
    #Se o login não está na lista, devolve sem alteração! 
    if login not in lista:
        print('oi')
        return login
    #Login está na lista! 
    else:
        #Percorrendo a lista!
        for logins in lista:
            print (lista[-1][-1])
            #Se o login for igual e ele for um número:
            if login == logins and logins[-1] not in string.ascii_lowercase:
                numero = int(logins[-1]) + 1
                login = login + numero
                return login
            #Se o login for igual e ele não for um número
            elif login == logins and logins[-1] in string.ascii_lowercase:
                numero = '1'
                login = login + numero
                return login