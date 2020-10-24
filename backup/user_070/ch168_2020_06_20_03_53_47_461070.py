def login_disponivel(novo, lista):
    for login in lista:
        if novo == login:
            novo = novo + '1'
            break
    for login in lista:
        if novo == login:
            lastnovo = int(novo[-1]) + 1
            lastnovo = str(lastnovo)
            novo[-1] = lastnovo
    return novo