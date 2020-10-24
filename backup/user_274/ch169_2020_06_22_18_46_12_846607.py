def login_disponivel(login, lista):
    c = 0
    if login not in lista:
        return login
    else:
        for i in lista:
            if i[:len(login)] == login:
                 c = c+1  
        return login+str(c)

list = []
new = input("Qual seu login? ")
while new != "fim":
    login = login_disponivel(new, list)
    list.append(login)
    new = input("Qual seu login? ")
    
print(list)