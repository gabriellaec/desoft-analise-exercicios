def login_disponivel(login, listalogin):
    i = 1
    if login not in listalogin:
        listalogin.append(login)
    else:
        login = login + str(i)
        i += 1
    return login


	while login != "fim" and not listalogin:
    	login = input("Digite o login desejado: ")
    	print(login)
    
    
listalogin = ["alex", "fabio", "pedro"]
login = alex