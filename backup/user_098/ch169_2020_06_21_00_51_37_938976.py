def login_disponivel(user, lista_logins):
  if not user in lista_logins:
    return user
  else:
    i=1
    while i>i-1:
      new_user=user+str(i)
      if not new_user in lista_logins:
        return new_user
      else:
        i+=1

logins = []
loop = True
while loop:
    name = input('digite seu login: ')
    if name == 'fim':
        break
    print(login_disponivel(name, logins))
    logins.append(login_disponivel(name, logins))