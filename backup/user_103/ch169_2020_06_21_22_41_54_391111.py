def login_disponivel(login,lista_registros):
    if login not in lista_registros:
        return login
    else:
        for i in range(len(lista_registros)):
            lista=[]
            user = str(lista_registros[i][0:len(login):1])
            if user == login:
                lista.append(user)
        return user+str(len(lista))
    
loginn = input('Qual é o seu login?')
users= [loginn]
while loginn != 'fim':
    loginn= input('Qual é o seu login?')
    user_certo = login_disponivel(loginn, users)
    users.append(user_certo)
for i in range(len(users)):
    print(users[i])


      