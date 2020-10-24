def login_disponivel(x,usuarios):
    for i in range(len(usuarios)):
        if x in usuarios:
            usuarios.append(x+'1')
            return usuarios
        if x not in usuarios:
            return x