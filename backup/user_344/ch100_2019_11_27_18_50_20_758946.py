def login_disponivel(lista):
	login = input('Qual é o seu login? ')
	lista.append(login)
	while login != 'fim':
	    login = input('Qual é o seu login? ')
	    i=1
        if login in lista:
            login = login + str(i)
            i+=1
            lista.append(login)
        
        else:
            lista.append(login)
     
    print(lista)