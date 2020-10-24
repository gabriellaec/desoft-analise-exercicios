def login_disponivel(login,usuarios):
    if login not in usuarios:
        usuarios.append(login)
        return login
    else:
        i = 0 
        for utilizado in usuarios:
            if utilizado[:len(login)]==login:
                i += 1
        return login+"{}".format(i)

pergunta =input("Seu Nome de usuario ?")
logins = []
while pergunta != 'fim':
    usuario_disponivel = login_disponivel(pergunta,logins)
    logins.append(usuario_disponivel)
    pergunta =input("Seu Nome de usuario ?")

for user in logins:
    if user !== 'fim'
    print(user)