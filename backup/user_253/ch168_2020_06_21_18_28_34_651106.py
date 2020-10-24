def login_disponivel(nome, lista):
    i+=0
    if nome not in lista:
        return nome
    else:
        while nome in lista:
            nome = (nome)i
        return nome