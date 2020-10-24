def login_disponivel(login,lis_login):
    cont = 1
    x = login
    for i in lis_login:
        if i == x:
            numero = str(cont)
            x = login + numero
            cont +=1
    return x
nome = 0
lis_login = []
while nome != 'fim':
    nome = input('qual o seu login? ')
    nome_correto = login_disponivel(nome,lis_login)
    lis_login.append(nome_correto)

for i in range(len(lis_login)-1):
    print(lis_login[i])