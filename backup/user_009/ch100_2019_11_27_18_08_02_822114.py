nome = input('digite um login: ')
lista_ = []
lista_.append(login_disponivel(nome, logins))

while nome != 'fim':
    nome = input('digite um login: ')
    login_disponivel(nome, logins)
    lista_.append(login_disponivel(nome, logins))

for i in lista_:
    print(i)
