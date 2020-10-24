import string 
def login_disponivel(login, lista):
    for logins in lista:
        if login not in lista:
            print('oi')
            return login
        else:
            print (lista[-1][-1])
            if lista[-1][-1] in list(string.ascii_lowercase) or lista[-1][-1] in list(string.ascii_uppercase):
                numero = '1'
                login = login + numero
                return login 
            else:
                numero = int(lista[-1][-1]) + 1
                login = login + str(numero)
                return login 