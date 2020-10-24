def login_disponivel(nome, lista):
    if not nome in lista:
        return nome
    else:
        i = 0
        for usuario in lista:
            if usuario.find(nome) == 0 :
                usuario = nome + '{0}'.format(i)
                i += 1
        return nome + i