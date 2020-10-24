def login_disponivel(nome, lista):
    i=1
    if nome not in lista:
        return nome
    else:
        for name in range(len(lista)):
            while nome in lista:
                nome = nome +str(i)
                if nome in lista:
                    nome= nome[:-1]
                i+=1
            return nome
state = True
logins = []
while state:
    login = input('Digite o login: ')
    if login != 'fim':
        login = login_disponivel(login,logins)
        logins.append(login)
        print(login)
    else:
        state = False