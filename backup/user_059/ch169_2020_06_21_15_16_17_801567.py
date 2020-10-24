def login_disponivel(login, lista):
    if login not in lista:
        return login
    else:
        cont = 0
        for i in lista:
            if login in i:
                cont +=1
        return login+str(cont)

pergunta = True
lista_login = []

while pergunta:
    login = input("Digite o login: ")
    if login == "fim":
        break
    else:
        lista_login.append(login_disponivel(login, lista_login))

for i in lista_login:
    print(i)