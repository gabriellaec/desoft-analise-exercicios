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

user = input('Qual é o seu login?')
users=[user]  
if user == 'fim':
    return ==[]
while user != 'fim':
    c=input('Qual é o seu login?')
    users.append(c)

for i in range(len(users)):
    b=login_disponivel(user[i],users)
    print (b)
      