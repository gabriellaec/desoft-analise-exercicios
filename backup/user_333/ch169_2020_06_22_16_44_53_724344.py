def login_disponivel(nome,lista):
    if nome not in lista:
        return nome
    disponivel = False
    n=1
    novo_login = nome
    while not disponivel:
        if novo_login not in lista:
            disponivel = True
        else:
            novo_login = nome + str(n)
            n+=1
            
    return novo_login

lista=[]
respondendo = True
while respondendo:
    nome = input('seu login')
    if nome == 'fim'
        respondendo = False
    else:
        login = login_disponível(nome,lista)
        lista.append(login)
        print(login)