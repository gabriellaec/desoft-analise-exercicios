def login_disponivel(login, lista_logins):
    i = 1
    if login not in lista_logins:
        return login
    else:
        return lista_login[login] + "i"

lista = []
login = input("Digite um login: ")
while login != 'fim':
    e = login_disponivel(login, lista)
    lista.append(e)
    login = input("Digite um login: ")
for ele in lista:
    print(ele) 

    
