def login_disponivel(nome, lista):
    if not nome in lista:
        return nome
    else:
        i = 0
        for usuario in lista:
            if usuario.find(nome) == 0 :
                usuario = nome + '{0}'.format(i)
                i += 1
        final = nome + '{0}'.format(i)
        return final

login = input('Digite um login: ')

todos = []
while login != 'fim':
    todos.append(login_disponivel(login, lista))
    login = input('Digite um login: ')
for i in todos:
    print(i)