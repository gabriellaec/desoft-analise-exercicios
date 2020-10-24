fim = True

def login_disponivel(usuario, lista):
    i = 1
    login = usuario
    for nome in lista:
        if login == nome:
            login = usuario + str(i)
            i += 1
    return login

lista_users = []
while fim:
    name = str(input('digite um nome de usuário: '))
    if name == 'fim':
        fim = False
    else:
        if not lista_users:
            lista_users.append(name)
        else:
            novo_nome = login_disponivel(name, lista_users)
            lista_users.append(novo_nome)

for users in lista_users:
    print(users