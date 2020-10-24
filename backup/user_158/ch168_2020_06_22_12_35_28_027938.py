def login_disponivel(login,usuarios):
    for i in range(0,len(usuarios)):
        if login == usuarios[i]:
            usuario_disponivel = login + str(i+1)
        else:
            usuario_disponivel = login
    return usuario_disponivel