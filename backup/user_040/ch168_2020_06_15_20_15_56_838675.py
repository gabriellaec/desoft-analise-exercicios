def login_disponivel(nome, login):
    x = 0
    for usuarios in login:
        if nome == usuarios:
            nome += "1"
    return nome
            