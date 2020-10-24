def login_disponivel(login,lista):
    login = input('Qual é o seu login? ')
    i=1
    if login in lista:
        login1 = login + str(i)
        lista.append(login1)
    else:
        lista.append(login)