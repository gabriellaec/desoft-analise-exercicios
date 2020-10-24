def login_disponivel(usuario,logins):
    repetido = False
    for i in logins:
        if usuario == i:
            repetido = True
    i = 1
    while repetido:
        user = usuario
        user += '{0}'.format(i)
        for i in logins:
            if usuario == i:
                repetido = True
            else:
                repetido = False
        i += 1
    return usuario
            