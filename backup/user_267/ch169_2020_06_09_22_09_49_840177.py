def login_disponivel(login, lista_logins):
    i = 1
    if login not in lista_logins:
        return login
    else:
        return lista_login[login] + "i"

lista = []
login = input("Digite um login: ")
if login != 'fim':
    lista.append(login)
while login != 'fim':
    login = input("Digite um login: ")
    lista.append(login)
for ele in lista:
    print(ele) 

    
