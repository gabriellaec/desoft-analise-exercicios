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

lista = []
login = input("Digite um login: ")
while login != 'fim':
    e = login_disponivel(login, lista)
    lista.append(e)
    login = input("Digite um login: ")
for ele in lista:
    print(ele) 

    
