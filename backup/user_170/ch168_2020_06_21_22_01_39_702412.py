def login_disponivel(nome, lista):
    i = 1
    if nome in lista:
        for n in lista:
            if "{}{}".format(nome, i) not in lista:
                return "{}{}".format(nome,i)
            i += 1

    
    else:
        return nome