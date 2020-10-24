def login_disponivel(login,lista):
    list = ["1,2,3,4,5,6,7,8,9"]
    i=0
    if login not in lista:
        print("Login Disponivel")
        i=0
    elif login in lista:
        while login in lista:
            print ("login indisponivel")
            login = login + list[i]
            i+=1
    return login