x = input('Qual login você deseja ?: ')
lista = []
while x != 'fim':
    lista.append(login_disponivel(x,lista))
    x = input('Qual login você deseja ?: ')
for login in lista:
    print(login)