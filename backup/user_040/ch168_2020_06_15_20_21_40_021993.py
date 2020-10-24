def login_disponivel(nome, login):
    x = ["0","1","2","3","4","5","6","7","8","9"]
    for usuarios in login:
        if nome == usuarios:
            for numero in x:
                if numero in usuario:
                    r = int(numero) + 1
                    nome += "{0}".format(r)
    return nome
            