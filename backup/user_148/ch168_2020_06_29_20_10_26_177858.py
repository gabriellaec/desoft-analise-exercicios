def login_disponivel(nome, lista):
    if not nome in lista:
        return nome
    else:
        verdade = True
        i = 1
        while verdade:
            nome2 = nome + str(i)
            if not nome2 in lista:
                verdade = False
                return nome2
            else:
                i += 1
