def login_disponivel(login,lista_registros):
    if login not in lista_registros:
        return login
    elif login in lista_registros:
        a=lista_registros.count(login)
        return login+a

user = input('Qual é o seu login?')
users=[user]  
while user != 'fim':
    c=input('Qual é o seu login?')
    users.append(c)
    if user == 'fim':
        break
for i in range(len(users)):
    b=login_disponivel(user[i],users)
    print (b)
      