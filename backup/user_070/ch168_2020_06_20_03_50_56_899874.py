def login_disponivel(novo, lista):
    for login in lista:
        if novo == login:
            novo = novo + '1'
            break
    for login in lista:
        if novo == login:
            novo[-1] = str(int(novo[-1])+1)
    return novo