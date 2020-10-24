def login_disponivel(login, lista_logins):
    if login in lista_logins:
        for i in range(1, len(lista_logins)):
            if '{0}{1}'.format(login, i) not in lista_logins:
                return '{0}{1}'.format(login, i)
    else:
        return login

texto = ''

while texto != 'fim':
    texto = str(input('Escreva um usuário: '))
    print(login_disponivel(texto))