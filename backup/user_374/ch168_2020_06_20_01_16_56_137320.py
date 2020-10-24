def login_disponivel(usuario, lista_usuarios):
    var_usuario = usuario
    lista = lista_usuarios
    contador = 1

    for i in lista:
        if var_usuario == i:
            var_usuario = usuario + str(contador)
            contador += 1
        else:
            lista.append(var_usuario)

    return var_usuario