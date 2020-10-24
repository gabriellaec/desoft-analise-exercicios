def login_disponivel(usuario, lista):
    i = 1
    login = usuario
    for nome in lista:
        if login == nome:
            login = usuario + str(i)
            i += 1
    return login

fim = True

lista_usuario = []
while fim:
    novo_usuario = input('Qual usuário? ')
    if novo_usuario == 'fim':
        fim = False
    else:
        if not lista_usuario:
            lista_usuario.append(novo_usuario)
        else:
            novo_login = login_disponivel(novo_usuario, lista_usuario)
            lista_usuario.append(novo_login)

for todo_usuario in lista_usuario:
    print(todo_usuario)