def login_disponivel(login,lista):
    for i in lista:
        if login not in lista:
            return login
        else:
            contador = 0
            for nome in lista:
                if nome[0:len(login)] == login:
                    contador += 1
            return login + str(contador)

perguntar = True
listanomes = ['']
listalogins = []
while perguntar == True:
    entrada = input('Digite nome: ')
    if entrada == 'fim':
        perguntar = False
    else:    
        login = (login_disponivel(entrada, listanomes))
        listanomes.append(entrada)
        listalogins.append(login)

for i in listalogins:
    print(i)