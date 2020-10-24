def login_disponivel(login, lista_logins):
    i = 1
    if login not in lista_logins:
        return login
    else:
        for a in range(len(lista_logins)):
            if login + "{0}".format(i) not in lista_logins:
                return login + "{0}".format(i)
            else:
                i += 1
                return login + "{0}".format(i)
            
nome = input('Digite o nome: ')
while nome != 'fim':
    usa = login_disponivel(nome, lista_logins)
    nome = input('Digite o nome: ')
for log in lista_logins:
    print(log)
    

    
