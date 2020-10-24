lista = []

while True:
    login = input('digite um login:')
    lista.append(login)
    if login == 'fim':
        break
    print(login_disponivel(login,lista))