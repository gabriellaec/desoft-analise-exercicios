def login_disponivel(novo, lista):
    for login in lista:
        if novo == login:
            novo = novo + '1'
            break
    x = '2'
    novo1 = ''
    for login in lista:
        if novo == login:
            for i in range(len(novo)-1):
                novo1 += novo[i]
            novo1 += x
            x = str(int(x)+1)
    return novo1