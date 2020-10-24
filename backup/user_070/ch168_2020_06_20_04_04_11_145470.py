def login_disponivel(novo, lista):
    for login in lista:
        if novo == login:
            novo = novo + '1'
            break
    for login in lista:
        if novo == login:
            print(novo)
            novo[-1] = x
            print(novo)
            i = int(i) + 1
            x = int(x) + 1
            i = str(i)
            x = str(x)
    return novo