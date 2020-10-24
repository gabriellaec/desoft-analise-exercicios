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