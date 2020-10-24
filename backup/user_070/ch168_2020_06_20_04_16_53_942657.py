def login_disponivel(novo, lista):
    for login in lista:
        if novo == login:
            novo = novo + '1'
            break
    x = '2'
    for login in lista:
        if novo == login:
            novo1 = ''
            for i in range(len(novo)-1):
                novo1 += novo[i]
            novo1 += x
            novo = novo1
            x = str(int(x)+1)
    return novo