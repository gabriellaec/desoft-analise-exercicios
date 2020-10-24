def login_disponivel (login,lista):
    if login not in lista:
        return login
    else:
        for login1 in range(len(lista)):
            i = 1
            while login in lista:
                login = login + str(i)
                if login in lista:
                    login = login [:-1]
                i+=1    
            return login

lista1 = []
while True:
    x = str(input("Digite o login: "))
    if x != "fim":
        login_ = login_disponivel(x,lista1)
        lista1.append(login_)
    if x == "fim":
        print(lista1)
        break
        
