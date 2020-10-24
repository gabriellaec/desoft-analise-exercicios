def login_disponivel(login,lista_registros):
    i= 1
    usuario = login  
    for nome in lista_registros:
        if login == nome:
            login = usuario + str(i)
            i+=1
    return login

roda = True
lista_users = []
while roda:
    loginn = str(input('digite um nome de usuário: '))
    if loginn == 'fim':
        roda = False
    else:
        if loginn not in lista_users:
            lista_users.append(loginn)
        else:
            loginn_certo = login_disponivel(loginn, lista_users)
            lista_users.append(loginn_certo)

for users in lista_users:
    print(users)
      