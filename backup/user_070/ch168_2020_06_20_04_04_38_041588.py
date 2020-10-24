def login_disponivel(novo, lista):
    for login in lista:
        if novo == login:
            novo = novo + '1'
            break
    x = '2'
    for login in lista:
        if novo == login:
            print(novo)
            novo[-1] = x
            print(novo)
            x = int(x) + 1
            x = str(x)
    return novo