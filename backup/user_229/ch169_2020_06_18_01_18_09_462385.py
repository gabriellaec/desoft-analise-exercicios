def login_disponivel(login, lista_logins):
    if login in lista_logins:
        for i in range(1, len(lista_logins)):
            if '{0}{1}'.format(login, i) not in lista_logins:
                return '{0}{1}'.format(login, i)
    else:
        return login

texto = ''
lista = []

while texto != 'fim':
    texto = str(input('Escreva um usuário: '))
    lista.append(texto)
    
for i in lista:
    if i != 'fim':
        print(login_disponivel(i, lista))