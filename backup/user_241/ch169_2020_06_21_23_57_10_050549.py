def login_disponivel(login,lista):
    if login not in lista:
        return login
    else:
        i = 1
        while True:
            nome = login + str(i)
            if nome not in lista:
                return nome
            else:
                i += 1

x = input('Qual login você deseja ?: ')
lista = []
while x != 'fim':
    lista.append(login_disponivel(x,lista))
    x = input('Qual login você deseja ?: ')
for login in lista:
    print(login)