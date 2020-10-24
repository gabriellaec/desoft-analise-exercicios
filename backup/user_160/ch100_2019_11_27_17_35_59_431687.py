login = input('Qual o login que o usuário deseja usar?')
i = 1
lista = login_disponivel
while login != 'fim':
    if login not in lista:
        print(login)
    while login in lista:
        login = login*(i)
    print(login)
        