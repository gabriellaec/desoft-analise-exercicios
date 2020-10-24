logins = ["andre"]
numero = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
d = 0
login = input("login:")
while login != "fim":
    login = input("login:")
    for i in logins:
        if login != i:
            logins.append(login)
            print("seu login:", login)
        else:
            loginnovo = login+numero[d]
            logins.append(loginnovo)
            print("seu login:", loginnovo)
            d += 1