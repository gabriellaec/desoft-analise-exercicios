def login_disponivel(nome, lista):
    i=1
    if nome not in lista:
        return nome
    else:
        for x in range(len(lista)):
            while nome in lista:
                nome = nome +str(i)
                if nome in lista:
                    nome= nome[:-1]
                i+=1
            return nome
        
logins = []
ans = ''
while ans != 'fim':
    ans = input('login: ')
    if ans != 'fim':
        login = login_disponivel(ans, logins)
        logins.append(login)
        print(login)