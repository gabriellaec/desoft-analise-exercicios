def login_disponivel(novo, lista):
    for login in lista:
        if novo == login:
            novo = novo + '1'
            break
    i = '1'
    x = '2'
    for login in lista:
        if novo == login:
            novo.replace(i, x)
            i = int(i) + 1
            x = int(x) + 1
            i = str(i)
            x = str(x)
            print(i)
            print(x)
    return novo